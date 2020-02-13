import sqlite3, random, time
import mysql.connector
import RPi.GPIO as GPIO
from sqlite3 import Error
import threading


box_id = 1

### local counting
def count_vote(conn, vote):
	try:
		c = conn.cursor()
		if vote:
			c.execute(""" UPDATE polls SET yes = yes + 1 WHERE poll_id='1'""")
		else:
			c.execute(""" UPDATE polls SET no = no + 1 WHERE poll_id='1'""")
		c.execute(""" UPDATE polls SET last_update = datetime('now') """)
	except Error as e:
		print(e)
	finally:
		conn.commit()

#def get_votes(c):
#	try:
#		c.execute(""" SELECT yes, no FROM polls """)
#		for row in c.fetchall():
#			print ("YES counts: " + str(row[0]))
#			print ("NO counts: " + str(row[1]))
#	except Error as e:
#		print(e)


def init_vote(c):
	vote_id = 1
	try:
		c.execute(""" INSERT INTO polls (box_id, poll_id, yes, no, last_update) VALUES("""+str(box_id)+""","""+str(vote_id)+""",0,0,datetime('now')); """)
	except Error as e:
		print(e)

def connect_db():

	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect('local_polls.db')
		try:
			c = conn.cursor()
			c.execute(""" CREATE TABLE IF NOT EXISTS polls (
											box_id integer, poll_id integer PRIMARY KEY,
											yes integer, no integer, last_update datetime
										); """)
			#init_vote(c)
		except Error as e:
			print(e)

	except Error as e:
		print(e)
	finally:
		if conn:
			conn.commit()
			#conn.close()
			return conn



### remote counting
vote_id = 1


def get_votes():
	""" create a database connection to a SQLite database """
	conn = None
	results = []
	try:
		conn = sqlite3.connect('local_polls.db')
		c = conn.cursor()
		try:
			c.execute(""" SELECT yes, no FROM polls WHERE box_id="""+str(box_id)+""" AND poll_id="""+str(vote_id))
			for row in c.fetchall():
				results.append(row[0])
				results.append(row[1])
				print ("GET VOTES: [BOX-ID]: " + str(box_id) + " [VOTE-ID]: "+ str(vote_id)+" [YES]: "+ str(row[0])+" [NO]: "+str(row[1]))

		except Error as e:
			print(e)

	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()
	return results


def push_votes(votes):
	if len(votes) > 0:
		try:
			cnx = mysql.connector.connect(user='citypolls', password='Hml8h30#',
										  host='kaigaertner.de',port=3306,
										  database='citypolls')
			mycursor = cnx.cursor()
			sql = " INSERT INTO boxes (boxid, pollid, yes, no, creation) VALUES (%s, %s, %s, %s, NOW()) "
			val = (box_id,vote_id,votes[0], votes[1])
			mycursor.execute(sql, val)
			cnx.commit()
			print(mycursor.rowcount, "record inserted.")
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		else:
			cnx.close()

def sync_votes():
	votes = []
	votes = get_votes()
	push_votes(votes)


### main programm ###

# database connection
conn = connect_db()

#button = random.choice((True, False))
#count_vote(conn, button)
#c = conn.cursor()
#get_votes(c)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulle$
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

clock = 1

while True: # Run forever
	if GPIO.input(10) == GPIO.LOW:
		print("Button YES was pushed!")
		count_vote(conn, True)
		time.sleep(.1)
		conn.commit()
		t = threading.Thread(name='child procs', target=sync_votes)
		t.start()
	if GPIO.input(12) == GPIO.LOW:
		print("Button NO was pushed!")
		count_vote(conn, False)
		time.sleep(.1)
		conn.commit()
		t = threading.Thread(name='child procs', target=sync_votes)
		t.start()
		# if ((clock % 5) == 0):
		#conn.commit()
		# if ((clock % 5) == 0):
		# t = threading.Thread(name='child procs', target=sync_votes)
		# t.start()
		#sync_votes()
	clock = clock+1
	time.sleep(.1)

conn.close()

