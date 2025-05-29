from mysql.connector import Error, IntegrityError
from database import get_connection


def add_product(name: str, category: str, quantity: int, price: float) -> str:
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    connection = get_connection()
    if connection is None:
        raise ConnectionError("Failed to connect to the database.")

    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO products (name, category, quantity, price)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, category, quantity, price))
        connection.commit()
        return f"Product '{name}' added successfully."

    except IntegrityError:
        raise ValueError(f"A product with the name '{name}' already exists.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def update_stock(product_id: int, delta: int) -> str:
    connection = get_connection()
    if connection is None:
        raise ConnectionError("Could not establish connection to the database.")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
        result = cursor.fetchone()

        if result is None:
            raise ValueError(f"No product found with ID {product_id}.")

        current_quantity = result[0]
        new_quantity = current_quantity + delta

        if new_quantity < 0:
            raise ValueError(
                f"Cannot reduce stock below zero. Current: {current_quantity}, attempted: {delta}."
            )

        cursor.execute(
            "UPDATE products SET quantity = %s WHERE id = %s",
            (new_quantity, product_id),
        )
        connection.commit()
        return f"Stock updated successfully. New quantity: {new_quantity}"

    except Error as e:
        raise RuntimeError(f"Error while updating stock: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def view_inventory() -> list:
    connection = get_connection()
    if not connection:
        raise ConnectionError("Failed to connect to the database.")

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, category, quantity, price, added_on, last_updated FROM products"
        )
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        raise RuntimeError(f"Error retrieving inventory: {e}")
    finally:
        cursor.close()
        connection.close()


def remove_product(product_id: int) -> str:
    connection = get_connection()
    if not connection:
        raise ConnectionError("Failed to connect to the database.")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        if not product:
            raise ValueError(f"No product found with ID {product_id}.")

        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        connection.commit()
        return f"Product with ID {product_id} removed successfully."

    except Exception as e:
        raise RuntimeError(f"Error removing product: {e}")
    finally:
        cursor.close()
        connection.close()
