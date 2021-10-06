# Create table

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

# sql = "CREATE TABLE student(stu_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), roll INT, fees FLOAT)"
sql1 = "SHOW TABLES"

myc = conn.cursor()
myc.execute(sql1)

for d in myc:
    print(d)

myc.close()
conn.close()