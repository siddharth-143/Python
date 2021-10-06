# Insert data in table

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

sql = 'INSERT INTO student(name, roll, fees) VALUES("karan", 102, 11000),("ventya", 103, 12000)'
sql1 = "SELECT * FROM student"

myc = conn.cursor()

try:
    myc.execute(sql1)
    # conn.commit()
    print("Data inserted")
    for d in myc:       # if you want ot display data
        print(d)

except:
    conn.rollback()
    print("Unable to process data")

myc.close()
conn.close()