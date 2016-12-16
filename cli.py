from datetime import datetime

import click

from tracker import Tracker


@click.group()
def cli():
    """Tracking time spent during tasks"""
    pass


@cli.command()
def status():
    """Status of the currently tracked task"""
    result = """
    Running task: <task_name>
         Started: 12/06/16 04:23 PM EST
        Duration: 1 hour, 12 minutes
    """
    click.echo(result)


@cli.command()
@click.argument("task")
def start(task_name):
    """Start tracking a task"""
    # storage format: task_name,start_date,end_date

    # stop()
    task = Task(task_name)
    tracker = Tracker(task)

    # start_date = datetime.today().strftime("%m/%d/%y %I:%M %p %Z")
    # click.echo("{0} started at {1}".format(task, start_date))
    # with open("task_store.csv", "a") as f:
    #     f.write("{0},{1},\n".format(task, start_date))


@cli.command()
def stop():
    """Stop tracking the current task"""
    result = """
    <task_name> stopped
        Time: 11:30 AM -- 02:31 PM EST
    Duration: 3 hours, 1 minute
    """
    click.echo(result)
