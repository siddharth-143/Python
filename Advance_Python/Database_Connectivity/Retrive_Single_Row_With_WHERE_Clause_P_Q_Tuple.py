# Retrieve multiple row with where clause parameterized query tuple

import mysql.connector

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

sql = 'SELECT * FROM student WHERE stu_id=%s'       # tuple
sql = 'SELECT * FROM student WHERE stu_id=%(id)s'           # dictionary
myc = conn.cursor()
i = int(input("Enter student Id : "))
# disp_val = (i, )      # tuple
disp_val = {"id": i}        # dictionary

try:
    myc.execute(sql, disp_val)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print("Total Rows : ", myc.rowcount)

except:
    conn.rollback()
    print("Unable to process data")

myc.close()
conn.close()