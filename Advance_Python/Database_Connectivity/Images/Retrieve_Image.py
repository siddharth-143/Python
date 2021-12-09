# Python program to Retrive image from database

import mysql.connector

def write_file(data, filename):
    # converting binary data to proper format and write it on disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBlob(name, photo):
    try:
        # establishing the connection
        conn = mysql.connector.connect(
            user="root",
            password="password",
            host="localhost",
            database="Image",
            port=3306
        )
        if conn.is_connected():
            print("Connected Successfully..!")

        cursor = conn.cursor()
        sql_query = "SELECT * FROM my_table where name = %s"

        cursor.execute(sql_query, (name,))
        record = cursor.fetchall()

        for row in record:
            print("Name = ", row[0])
            image = row[1]
            file = row[0]
            print("Storing Image...")
            write_file(image, photo)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MYSQL {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

readBlob("mama", "2.jpeg")