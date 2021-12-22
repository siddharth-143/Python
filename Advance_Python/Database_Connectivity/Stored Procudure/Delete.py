# Python program to implement delete query using stored Procedure

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

cur.callproc('stuDelete', [1])
conn.commit()
print("Data delete successfully....")
cur.execute("SELECT * FROM student")
print(cur.fetchall())

cur.close()
conn.close()