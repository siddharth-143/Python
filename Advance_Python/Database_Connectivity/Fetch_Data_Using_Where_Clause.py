# Fetch data from table with WHERE Clause

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

sql = 'SELECT * FROM student WHERE stu_id=11'        # write a sql query
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    print(row)
    print("Row Count : ", myc.rowcount)

except:
    conn.rollback()
    print("Unable to update data")

myc.close()
conn.close()