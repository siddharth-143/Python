# Fetch data from table using fetchall() method

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

sql = 'SELECT * FROM student'
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchall()
    for r in row:
        print(r)
    print("Total Rows : ", myc.rowcount)

except:
    conn.rollback()
    print("Unable to process data")

myc.close()
conn.close()