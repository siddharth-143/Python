# Fetch data from table using fetchmany() method

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
myc = conn.cursor(buffered=True)

try:
    myc.execute(sql)
    row = myc.fetchmany(size=3)         # fetchmany method
    for r in row:
        print(r)
    print("Total Rows : ", myc.rowcount)
    print()
    row = myc.fetchall()            # fetchall method
    for r in row:
        print(r)
    print("Remaining Rows : ", myc.rowcount)

except:
    conn.rollback()
    print("Unable to process data")

myc.close()
conn.close()