# Project: Help yourself city

Creating a real life usable voting plattform for local issues. Based on a Raspberry Pi Zero WH, an UMTS module, a powerbank and self made casing out of acryl, it can be put nearly anywhere to vote on a given topic by up- or downvoting.

## Server implemenation
The project uses a simple MySQL database to store the votes over a predefined period of time and can present them via a website. A running prototype could be found at: cit

## UrbanAnt

### Casing
The casing consists of laser cut acryl and 3D printed parts, some buttons, cables and LEDs for the interior. It provides enough space for the Raspberry Pi Zero WH, the UMTS module and a battery.
The case consists of laser cut and 3D-printed parts. The necessary files are included in the folders named correspondingly. 

## Programming
The control programm is written for Python 3 running on Raspbian Buster on the Rasperry Pi. All functionalities can be found in the *box.py* which runs as a service after powering up the device.
The votes are stored locally in a sqlite database and can be commited to the MySQL server in e predefined interval. The only additional dependencies for the programm are the [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) package and [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) which can be installed using:
```bash
pip3 install mysql-connector-python RPi.GPIO
```
For the voting a delay can be set to avoid abusive usage by voting rapidly.
