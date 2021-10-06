# Update data

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

sql = 'UPDATE student SET fees=200 WHERE stu_id=5'
myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Row Update")

except:
    conn.rollback()
    print("Unable to update data")

myc.close()
conn.close()