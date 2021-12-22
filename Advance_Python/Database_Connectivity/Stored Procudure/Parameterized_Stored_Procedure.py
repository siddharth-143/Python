# Python program to implement Parameterized Stored Procedure

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
    print("Unable to connect ", error)

cur = conn.cursor()
cur.callproc('para', [1])

print("-----------------Student Details-----------------")
for result in cur.stored_results():
    slist = result.fetchall()
    for row in slist:
        print(row)

cur.close()
conn.close()