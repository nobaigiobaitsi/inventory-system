from product_ops import (
    add_product as db_add_product,
    update_stock as db_update_stock,
    view_inventory as db_view_inventory,
    remove_product as db_remove_product,
)


def add_product(name: str, category: str, quantity: int, price: float):
    if not name.strip():
        raise ValueError("Product name cannot be empty.")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    db_add_product(name, category, quantity, price)


def update_product_stock(product_id: int, delta: int):
    if not isinstance(product_id, int) or product_id <= 0:
        raise ValueError("Product ID must be a positive integer.")
    if delta == 0:
        raise ValueError("Delta must not be zero.")

    db_update_stock(product_id, delta)


def remove_product(product_id: int):
    if not isinstance(product_id, int) or product_id <= 0:
        raise ValueError("Product ID must be a positive integer.")

    db_remove_product(product_id)


def get_inventory():
    return db_view_inventory()
