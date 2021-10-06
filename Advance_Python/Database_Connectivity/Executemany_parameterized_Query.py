# Insert data into table using executemany parameterized query tuple

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

sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'        # parameterized query
myc = conn.cursor()
sql_of_params = [("omesh", 115, 1002), ("jay", 116, 20001), ("veer", 117, 1271), ("basanti", 119, 3223)]           # parameterized query

try:
    myc.executemany(sql, sql_of_params)
    conn.commit()           # committing the change
    print(myc.rowcount, "Row")           # Number of rows inserted

except:
    conn.rollback()         # Rollback the change
    print("Unable to update data")

myc.close()         # close cursor
conn.close()        # close connection
