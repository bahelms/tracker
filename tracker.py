import click

@click.group()
def cli():
    """Tracking time spent during tasks"""
    pass

@click.command()
def status():
    """Status of the currently running task."""
    click.echo("No currently running tasks.")

cli.add_command(status)

if __name__ == "__main__":
    cli()
