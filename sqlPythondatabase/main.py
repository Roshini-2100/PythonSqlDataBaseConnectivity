from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host="127.0.0.1", user="root", password="Qwerty@123", database="pysql_db" )

def insert(name,age,city):
    res = con.cursor()
    sql = "insert into users(name, age, city) values(%s, %s, %s)"
    users = (name, age, city)
    res.execute(sql,users)
    con.commit()
    print("Data Inserted")


def update(name,age,city,id):
    res = con.cursor()
    sql = "update users set name=%s, age=%s, city=%s where id=%s"
    users = (name, age, city, id)
    res.execute(sql,users)
    con.commit()
    print("Data Updated")


def select():
    res=con.cursor()
    sql = "SELECT * from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID","NAME","AGE","CITY"]))
def delete(id):
    res = con.cursor()
    sql = "delete into users where id=%s"
    users = (id)
    res.execute(sql, users)
    con.commit()
    print("Data Updated")

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Quit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        name =input("Enter Name: ")
        age =input("Enter age: ")
        city =input("Enter City :")
        insert(name,age,city)

    elif choice ==2:
        id =input("Enter Id: ")
        name =input("Enter name: ")
        age =input("Enter age: ")
        city = input("Enter City: ")
        update(name, age, city, id)
    elif choice == 3:
        select()

    elif choice ==4:
        id=input("Enter the id: ")
        delete(id)

    elif choice ==5:
        quit()

    else:
        print("Invalid Operation.Try Again")