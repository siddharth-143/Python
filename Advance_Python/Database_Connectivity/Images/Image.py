# Create and show database

import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="password",
        host="localhost",
        database="Image",
        port=3306
    )
    if conn.is_connected():
        print("Connect Successfully")

except:
    print("Unable to connect")

sql = "CREATE TABLE my_table (name TEXT, photo BLOB)";

myc = conn.cursor()
myc.execute(sql)

myc.close()
conn.close()