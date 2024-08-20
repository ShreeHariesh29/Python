import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="abc123"
)

print(mydb)
