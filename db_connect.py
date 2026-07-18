import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # We use 127.0.0.1 instead of 'localhost' to force TCP/IP
    connection = mysql.connector.connect(
        host="127.0.0.1", 
        port=3306,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    if connection.is_connected():
        print("Successfully connected to the database!")
        connection.close()
except Exception as e:
    print(f"Error: {e}")