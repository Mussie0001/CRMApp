import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'pass3456'

	)

cursorObject = dataBase.cursor()

# Database creation
cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")