# Insert dataa into table parametrized query using dictionary

import mysql.connector

try:
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

sql = 'INSERT INTO student(name, roll, fees) VALUES(%(n)s, %(r)s, %(f)s)'
myc = conn.cursor()
params = {'n': "Python", 'r': 124, 'f': 232}
try:
    myc.execute(sql, params)
    conn.commit()           # Committing the change
    print(myc.rowcount, "Row Inserted")         # Number of Row Inserted
    print(f"Stu ID : {myc.lastrowid} Inserted")         # Last inserted ID

except:
    conn.rollback()         # Rollback the change
    print("Unable to process data")

myc.close()         # close cursor
conn.close()        # close connection

