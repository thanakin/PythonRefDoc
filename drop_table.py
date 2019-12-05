import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

'''
print('\n Delete a Table')
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
'''

print('\n Drop Only if Exist')
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)