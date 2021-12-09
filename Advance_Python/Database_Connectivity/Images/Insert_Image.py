# Python program to insert image in database

import mysql.connector


def convertToBinaryData(filename):
    # convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(name, photo):
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
        sql_blob_query = "INSERT INTO my_table(name, photo) VALUES (%s, %s)"

        # converting human readable file into binary format
        empPhoto = convertToBinaryData(photo)

        # convert data into tuple format
        blob_tuple = (name, photo)

        # executing the query
        result = cursor.execute(sql_blob_query, blob_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB in to table")

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MYSQL table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


insertBLOB("Mama", "2.jpeg")
