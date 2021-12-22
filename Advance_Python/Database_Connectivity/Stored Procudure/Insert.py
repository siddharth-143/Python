# Python program to implement insert operation using stored Procedure

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='',
        database='school',
        host='localhost',
        port=3306
    )
    if conn.is_connected():
        print("Connected Successfully...!")

except mysql.connector.Error as error:
    print("Unable to connected ", error)

cur = conn.cursor()

cur.callproc('stuInsert', ['parshuram', 106, 'BBA', 50000])
conn.commit()

print("-----------------Student Details-----------------")
cur.execute("SELECT * FROM student")
print(cur.fetchall())

cur.close()
conn.close()