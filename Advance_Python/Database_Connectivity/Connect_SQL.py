# create check and close database connection

import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="password",
        host="localhost",  # by default optional
        port=3306  # by default optional
    )
    if conn.is_connected():  # used to check the connection is connected or not with sql
        print("Connect Successfully")

except:
    print("Unable To Connect The Server")

print("Before close : ", conn.is_connected())
c = conn.close()
print("After close : ", conn.is_connected())
