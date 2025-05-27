import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        if connection.is_connected():
            print("Successfully connected to Database!")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
