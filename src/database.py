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


def add_product(name: str, category: str, quantity: int, price: float) -> None:
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    connection = get_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO products (name, category, quantity, price)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, category, quantity, price))
        connection.commit()
        print(f"Product '{name}' added successfully.")
    except mysql.connector.IntegrityError as e:
        print(f"Error: A product with the name '{name}' already exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def update_stock(product_id: int, quantity_change: int) -> None:
    pass


def view_inventory() -> list[dict]:
    pass


def remove_product(product_id: int) -> None:
    pass
