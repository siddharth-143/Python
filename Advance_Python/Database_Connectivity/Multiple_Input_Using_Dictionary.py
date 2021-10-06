# Insert multiple data into table using execute parametrized query using dictionary

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

    sql = 'INSERT INTO student(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)'
    myc = conn.cursor()
    n = nm
    r = ro
    f = fe
    params = {"name":n, "roll": r, "fees": f}
    try:
        myc.execute(sql, params)            # Execute
        conn.commit()           # Committing the change
        print(myc.rowcount, "Row Inserted")         # Number of Row Inserted
        print(f"Stu ID : {myc.lastrowid} Inserted")         # Last inserted ID

    except:
        conn.rollback()         # Rollback the change
        print("Unable to process data")

    myc.close()         # close cursor
    conn.close()        # close connection

while True:
    # Data input from user
    nm = input("Enter Name : ")
    ro = int(input("Enter Roll : "))
    fe = int(input("Enter Fees : "))
    student_data(nm, ro, fe)
    ans = input("Do You Want To Exit : (y/n)")
    if ans == "y":
        break



