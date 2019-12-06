import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

print('\n Check if Table Exists')

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

print('\n Primary Key')
# create table with Primary Key
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

'''
print('\n Primary Key')
# alter table to include Primary Key
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
'''