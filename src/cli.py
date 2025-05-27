import click
from inventory import (
    add_product as cmd_add_product,
    update_product_stock as cmd_update_stock,
    get_inventory as cmd_view_inventory,
    remove_product as cmd_remove_product,
)


@click.group()
def cli():
    """Inventory Management CLI."""
    pass


@cli.command()
@click.argument("name")
@click.option("--category", default="", help="Category of the product.")
@click.argument("quantity", type=int)
@click.argument("price", type=float)
def add(name, category, quantity, price):
    """Add a new product."""
    try:
        cmd_add_product(name, category, quantity, price)
    except ValueError as ve:
        click.echo(f"Validation Error: {ve}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
def view():
    """View current inventory."""
    try:
        inventory = cmd_view_inventory()
        if not inventory:
            click.echo("Inventory is empty.")
            return
        for product in inventory:
            click.echo(product)
    except Exception as e:
        click.echo(f"Error retrieving inventory: {e}")


@cli.command()
@click.argument("product_id", type=int)
@click.argument("delta", type=int)
def update_stock(product_id, delta):
    """Update stock quantity for a product by delta."""
    try:
        cmd_update_stock(product_id, delta)
        click.echo(f"Stock for product ID {product_id} updated by {delta}.")
    except ValueError as ve:
        click.echo(f"Validation Error: {ve}")
    except Exception as e:
        click.echo(f"Error updating stock: {e}")


@cli.command()
@click.argument("product_id", type=int)
def remove(product_id):
    """Remove a product from inventory."""
    confirm = click.confirm(
        f"Are you sure you want to remove product ID {product_id}?", default=False
    )
    if confirm:
        try:
            cmd_remove_product(product_id)
            click.echo(f"Product ID {product_id} removed.")
        except Exception as e:
            click.echo(f"Error removing product: {e}")
    else:
        click.echo("Operation cancelled.")


if __name__ == "__main__":
    cli()
