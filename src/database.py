import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import logging
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        if connection.is_connected():
            logging.info("Successfully connected to Database!")
            return connection
    except Error as e:
        logging.error(f"Error while connecting to MySQL: {e}")
        return None
