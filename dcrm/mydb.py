# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Deaath@65',
)


# prepare a cursor object
cursorObject = dataBase.cursor()



# create a database
cursorObject.execute("CREATE DATABASE CRM")

print("database created")
