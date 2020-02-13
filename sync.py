import mysql.connector
from mysql.connector import errorcode

import sqlite3
from sqlite3 import Error

box_id = 1
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
			print ("BOX-ID: " + str(box_id))
			print ("VOTE-ID: " + str(vote_id))
			for row in c.fetchall():
				print ("YES counts: " + str(row[0]))
				results.append(row[0])
				print ("NO counts: " + str(row[1]))
				results.append(row[1])
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
		
votes = []
votes = get_votes()

push_votes(votes)


