import click
from product_ops import add_product, update_stock, view_inventory, remove_product


@click.group()
def cli():
    """Inventory Management CLI."""
    pass


@cli.command()
@click.argument("name")
@click.option("--category", default="", help="Category of the product.")
@click.argument("quantity", type=int)
@click.argument("price", type=float)
def cmd_add(name, category, quantity, price):
    """Add a new product."""
    add_product(name, category, quantity, price)
    click.echo(f"Product '{name}' added successfully.")


@cli.command()
def cmd_view():
    """View current inventory."""
    inventory = view_inventory()
    for product in inventory:
        click.echo(product)


@cli.command()
@click.argument("product_id", type=int)
@click.argument("delta", type=int)
def cmd_update_stock(product_id, delta):
    """Update stock quantity for a product by delta."""
    update_stock(product_id, delta)
    click.echo(f"Stock for product ID {product_id} updated by {delta}.")


@cli.command()
@click.argument("product_id", type=int)
def cmd_remove(product_id):
    """Remove a product from inventory."""
    confirm = click.confirm(
        f"Are you sure you want to remove product ID {product_id}?", default=False
    )
    if confirm:
        remove_product(product_id)
        click.echo(f"Product ID {product_id} removed.")
    else:
        click.echo("Operation cancelled.")


if __name__ == "__main__":
    cli()
