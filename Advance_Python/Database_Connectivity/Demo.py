import mysql.connector

# Creating the connection object     
conn_obj = mysql.connector.connect(
    user="root",
    password="password",
    host="localhost",
    database="pdb",
    port=3306,
)

# printing the connection object     
print(conn_obj)

# creating the cursor object    
cur_obj = conn_obj.cursor()

print(cur_obj)    