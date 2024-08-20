import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="employee"
    )
hand = mydb.cursor();
#hand.execute("update students set number = 1234567898 where name = 'Aarav'")
hand.execute("use employee")


def update():
    Nname = "Shiva"
    ID = 1002
    upquery = "update student set name = %s where id = %s"
    datas = (Nname,ID)
    hand.execute(upquery,datas)
    mydb.commit()
    print("data updated")

def insert():
    Id = int(input("Enter the id = "))
    name = input("Enter the name = ")
    dept = input("Enter the department = ")

    query = "insert into student(id,name,dept) values (%s, %s, %s)"
    data = (Id,name,dept)
    print(f"insert into student values ({Id},{name},{dept})")
    hand.execute(query,data)
    mydb.commit()
   
insert()
update()

hand.execute("select*from student")
for x in hand:
    print(x)

