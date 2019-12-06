import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

print('\n Join Two or More Tables')
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print('\n LEFT JOIN')
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print('\n RIGHT JOIN')
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)