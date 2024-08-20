import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123"
    )

cur = mydb.cursor()
cur.execute("create database if not exists ATM")
cur.execute("use atm")
cur.execute("create table if not exists userdata(ID int, name varchar(20), accno bigint, pin int)")

def insert(name,accno,pin):
    query="insert into userdata(ID,name,accno,pin) values(%s, %s, %s, %s)"
    i = 0
    cur.execute("select ID from userdata")
    for x in cur:
        for y in x:
            i = y
    i += 1
    data=(i,name,accno,pin)
    cur.execute(query,data)
    mydb.commit()

no = int(input("how many number of user u want to add = "))
for x in range(0,no):
    name = input("Enter your name")
    accno = int(input("Enter Your Account number = "))
    pin = int(input("Enter your new 4 digit pin = "))
    insert(name,accno,pin)

    
