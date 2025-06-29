import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals() and db.is_connected():
            db.close()
if __name__ == '__main__':
    create_database()