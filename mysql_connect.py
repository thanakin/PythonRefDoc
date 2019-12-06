'''
Download and install "MySQL Connector":

python -m pip install mysql-connector
or
python3 -m pip install mysql-connector
or
sudo apt-get install python3-mysql.connector
'''


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

print(mydb)
