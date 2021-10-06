# Fetch data from table

import mysql.connector

try :
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

sql = 'SELECT * FROM student'
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        # stu_id = row[0]
        # name = row[1]
        # roll = row[2]
        # fees = row[3]
        # print(f"Stud ID : {stu_id} Name : {name} Roll : {roll} Fees : {fees}")

        print(row)
        row = myc.fetchone()
    print("Total Rows : ", myc.rowcount)

except:
    conn.rollback()
    print("Unable to process data")

myc.close()
conn.close()