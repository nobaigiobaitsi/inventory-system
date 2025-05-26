import mysql.connector
from mysql.connector import Error





def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='inventory_db',
            user='root',
            password='Xfg1jlk..'
        )
        if connection.is_connected():
            print("Successfully connected to Database!")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None




def add_product(name: str, category: str, quantity: int, price: float) -> None:
    pass

def update_stock(product_id: int, quantity_change: int) -> None:
    pass

def view_inventory() -> list[dict]:
    pass

def remove_product(product_id: int) -> None:
    pass

