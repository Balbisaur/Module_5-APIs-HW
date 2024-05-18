import mysql.connector 
from mysql.connector import Error


def db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Amwbz2Fehrp6",
            database="library_system"
        )
        print("connected")
        return conn
    except Error as e:
        print(e)
        return None





