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
        message = cmd_add_product(name, category, quantity, price)
        click.echo(message)
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
        click.echo(
            f"{'ID':<5}{'Name':<25}{'Category':<15}{'Qty':<8}{'Price':<10}{'Added On':<20}{'Last Updated'}"
        )
        click.echo("-" * 95)
        for row in inventory:
            click.echo(
                f"{row[0]:<5}{row[1]:<25}{row[2]:<15}{row[3]:<8}{row[4]:<10}{row[5]:<20}{row[6]}"
            )
    except Exception as e:
        click.echo(f"Error retrieving inventory: {e}")


@cli.command()
@click.argument("product_id", type=int)
@click.argument("delta", type=int)
def update_stock(product_id, delta):
    """Update stock quantity for a product by delta."""
    try:
        message = cmd_update_stock(product_id, delta)
        click.echo(message)
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
            message = cmd_remove_product(product_id)
            click.echo(message)
        except Exception as e:
            click.echo(f"Error removing product: {e}")
    else:
        click.echo("Operation cancelled.")


if __name__ == "__main__":
    cli()
