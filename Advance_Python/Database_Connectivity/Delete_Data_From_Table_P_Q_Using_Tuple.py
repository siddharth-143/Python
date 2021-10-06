# Delete data from table parameterized query

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

sql = 'DELETE FROM student WHERE stu_id=%s'
myc = conn.cursor()
n = int(input("Enter Id to delete : "))
del_val = (n,)

try:
    myc.execute(sql, del_val)
    conn.commit()           # Committing the change
    print(myc.rowcount, "Row Delete")

except:
    conn.rollback()         # Rollback the change
    print("Unable to process data")

myc.close()         # close cursor
conn.close()            # close connection

