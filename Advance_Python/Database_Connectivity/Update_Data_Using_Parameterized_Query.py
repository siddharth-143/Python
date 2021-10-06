# Update data in table parametrized query

import mysql.connector

def student_data(id, nm, ro, fe):
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

    # sql = 'UPDATE student SET name=%s, roll=%s, fees=%s WHERE stu_id=%s'            # Using tuple
    sql1 = "UPDATE student SET name=%(n)s, roll = %(r)s, fees=%(f)s WHERE stu_id=%(i)s"     # using dictionary
    myc = conn.cursor()
    # update_val = (nm, ro, fe, id)
    update_val1 = {"i": id, "n": nm, "r": ro, "f": fe}

    try:
        myc.execute(sql1, update_val1)
        conn.commit()           # Committing the change
        print(myc.rowcount, "Row Update")

    except:
        conn.rollback()         # Rollback the change
        print("Unable to process data")

    myc.close()         # close cursor
    conn.close()            # close connection

while True:
    id = int(input("Enter student id to update : "))
    nm = input("Enter Name : ")
    ro = int(input("Enter Roll No : "))
    fe = int(input("Enter Fees : "))
    student_data(id, nm, ro, fe)
    ans = input("Do You Want To Exit (y/n) : ")
    if ans == "y":
        break