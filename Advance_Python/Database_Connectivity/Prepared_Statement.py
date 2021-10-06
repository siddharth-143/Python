# Prepared Statement

import mysql.connector


def student_data(fetch):       # def student_data(nm, ro, fe)
    try:
        conn = mysql.connector.connect(
            user="root",
            password="password",
            host="localhost",
            database="pdb",
            port=3306
        )
        if conn.is_connected():  # check the connection
            print("Connect Successfully")

    except:
        print("Unable To Connect")

    # sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'       # tuple
    # sql = 'INSERT INTO student(name, roll, fees) VALUES(%?, %?, %?)'
    # sql = 'DELETE FROM student WHERE stu_id=%s'
    # sql = 'UPDATE student SET fees=%s WHERE stu_id=%s'
    # sql = 'SELECT * FROM student WHERE stu_id=%s'
    sql = 'SELECT * FROM student WHERE fees=%s'

    myc = conn.cursor(prepared=True)  # cursor prepared method
    # n = nm
    # r = ro
    # f = fe
    # disp_val = (nm, ro, fe)

    # d = delete_data         # delete data
    # del_val = (delete_data, )              # tuple

    # f = fe
    # i = id
    # update_val = (fe, id)  # update data

    fat = fetch
    fetch_data = (fetch,)

    try:
        myc.execute(sql, fetch_data)  # execute query
        # conn.commit()  # committing the changes     (while fetching data no need of committing the change)

        # row = myc.fetchone()      # to display single row
        row = myc.fetchone()
        while row is not None:
            print(row)
            row = myc.fetchone()

        print(myc.rowcount, "Row inserted")

    except:
        conn.rollback()  # rollback the changes
        print("Unable to process data")

    myc.close()  # close cursor
    conn.close()  # close connection


while True:
    # nm = input("Enter Name : ")
    # ro = int(input("Enter Roll No : "))
    # fe = int(input("Enter Fees : "))
    # student_data(nm, ro, fe)          # call function student_data()

    # delete_data = int(input("Enter student id : "))
    # student_data(delete_data)

    # fe = int(input("Enter fees : "))
    # id = int(input("Enter Id : "))
    # student_data(fe, id)

    # fetch = int(input("Enter id to display data : "))
    # student_data(fetch)

    fetch = int(input("Enter fees : "))
    student_data(fetch)

    ans = input("Do you want to exit (y/n) : ")
    if ans == "y":
        break
