from mysql.connector import Error
from database import get_connection


def add_product(name: str, category: str, quantity: int, price: float):
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


def update_stock(product_id, delta):
    try:
        connection = get_connection()
        if connection is None:
            print("Could not establish connection to the database.")
            return

        cursor = connection.cursor()

        cursor.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"No product found with ID {product_id}.")
            return

        current_quantity = result[0]
        new_quantity = current_quantity + delta

        if new_quantity < 0:
            print(
                f"Cannot reduce stock below zero. Current stock: {current_quantity}, attempted change: {delta}."
            )
            return

        cursor.execute(
            "UPDATE products SET quantity = %s WHERE id = %s",
            (new_quantity, product_id),
        )
        connection.commit()
        print(f"Stock updated successfully. New quantity: {new_quantity}")

    except Error as e:
        print(f"Error while updating stock: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def view_inventory():
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, category, quantity, price, added_on, last_updated FROM products"
        )
        rows = cursor.fetchall()

        if rows:
            print(
                f"{'ID':<5}{'Name':<25}{'Category':<15}{'Qty':<8}{'Price':<10}{'Added On':<20}{'Last Updated'}"
            )
            print("-" * 95)
            for row in rows:
                print(
                    f"{row[0]:<5}{row[1]:<25}{row[2]:<15}{row[3]:<8}{row[4]:<10}{row[5]:<20}{row[6]}"
                )
        else:
            print("Inventory is empty.")

    except Exception as e:
        print(f"Error retrieving inventory: {e}")
    finally:
        cursor.close()
        connection.close()


def remove_product(product_id):
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()

        # Check if the product exists
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        if not product:
            print(f"No product found with ID {product_id}.")
            return

        # Delete the product
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        connection.commit()
        print(f"Product with ID {product_id} removed successfully.")

    except Exception as e:
        print(f"Error removing product: {e}")
    finally:
        cursor.close()
        connection.close()
