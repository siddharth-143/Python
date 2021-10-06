# Insert data into table using parameterized query tuple

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
params = ("dinesh", 114, 1001)            # parameterized query

try:
    myc.execute(sql, params)
    conn.commit()           # committing the change
    print(myc.rowcount, "Row Update")           # Number of rows inserted
    print(f"Stu Id : {myc.lastrowid} Inserted")

except:
    conn.rollback()         # Rollback the change
    print("Unable to update data")

myc.close()         # close cursor
conn.close()        # close connection
