# Insert data into table using executemany parametrized query using dictionary

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

sql = 'INSERT INTO student(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)'
myc = conn.cursor()

params = [
    {'name': "lenovo", 'roll': 33, 'fees': 400},
    {"name": "hp", "roll": 11, "fees": 100}
]
try:
    myc.executemany(sql, params)            # Execute
    conn.commit()           # Committing the change
    print(myc.rowcount, "Row Inserted")         # Number of Row Inserted
    print(f"Stu ID : {myc.lastrowid} Inserted")         # Last inserted ID

except:
    conn.rollback()         # Rollback the change
    print("Unable to process data")

myc.close()         # close cursor
conn.close()        # close connection



