# Create and show database

import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="password",
        host="localhost",
        # database="pdb",
        port=3306
    )
    if conn.is_connected():
        print("Connect Successfully")

except:
    print("Unable to connect")

sql1 = "CREATE DATABASE pdb"        # Create database
sql2 = "SHOW DATABASES"         # display database
sql3 = "SHOW TABLES"

myc = conn.cursor()
myc.execute(sql3)
for d in myc:
    print(d)


myc.close()
conn.close()