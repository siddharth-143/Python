# lastrowid Property

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

sql = 'INSERT INTO student(name, roll, fees) VALUES("raj", 108, 17000), ("rohan", 109, 20000)'          # insert multiple data into table

myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.lastrowid)

except:
    conn.rollback()
    print("Unable to process data")


myc.close()
conn.close()