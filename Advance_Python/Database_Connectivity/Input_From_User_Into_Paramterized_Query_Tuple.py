# Input from user into table parameterized query tuple

import mysql.connector

def student_data(nm, ro, fe):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="password",
            host="localhost",
            database="pdb",
            port=3306
        )
        if conn.is_connected():
            print("Connect Successfully")

    except:
        print("Unable To Connect")

    sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'        # parameterized query
    myc = conn.cursor()
    n = nm
    r = ro
    f = fe
    params = (n, r, f)            # parameterized query

    try:
        myc.execute(sql, params)
        conn.commit()           # committing the change
        print(myc.rowcount, "Row Update")           # Number of rows inserted
        print(f"Stu Id : {myc.lastrowid} Inserted")         # Last inserted ID

    except:
        conn.rollback()         # Rollback the change
        print("Unable to update data")

    myc.close()         # close cursor
    conn.close()        # close connection

while True:
    # input from user
    nm = input("Enter Name : ")
    ro = int(input("Enter Roll No : "))
    fe = int(input("Enter Fees : "))
    student_data(nm, ro, fe)
    ans = input("Do You Want to exit (y/n)")
    if ans == "y":
        break
