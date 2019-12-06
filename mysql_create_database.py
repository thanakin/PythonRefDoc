import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

#print('\n Create Database')
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

print('\n Check if Database Exists')

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

print('\n Try connecting to the database "mydatabase":')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

print(mydb)