from datetime import datetime

import click


@click.group()
def cli():
    """Tracking time spent during tasks"""
    pass


@cli.command()
def status():
    """Status of the currently running task."""
    click.echo("No currently running tasks.")


@cli.command()
@click.argument("task")
def start(task):
    """Start tracking a task"""
    start_date = "12/06/16 04:23 PM EST"
    click.echo("{} started at {}".format(task, start_date))
