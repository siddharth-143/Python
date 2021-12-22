import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='school',
        port=3306
    )
    if conn.is_connected():
        print("Connected Successfully...!")

except mysql.connector.Error as error:
    print("Unable to connected", error)

cur = conn.cursor()
cur.callproc('myselect')
print("-----------------Student Details-----------------")

for result in cur.stored_results():
    slist = result.fetchall()
    for row in slist:
            print(row)

cur.close()
conn.close()