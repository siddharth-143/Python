# Delete data from table

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

sql = 'DELETE FROM student WHERE stu_id=2'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Row Delete")

except:
    conn.rollback()
    print("Unable to process data")


myc.close()
conn.close()