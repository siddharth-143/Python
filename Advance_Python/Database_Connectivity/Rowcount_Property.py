# rowcount property

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

sql = 'INSERT INTO student(name, roll, fees) VALUES("suraj", 112, 17000), ("kaka", 110, 20000)'          # insert multiple data into table

myc = conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount, "Row inserted")

except:
    conn.rollback()
    print("Unable to process data")


myc.close()
conn.close()