import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


# open connection
def open_connection():

    try:

        connection = mysql.connector.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        return connection
    except Error as e:
        print('Error: ', e)


# close connection
def close_connection(connection, cursor):

    if connection:
        cursor.close()
        connection.close()
