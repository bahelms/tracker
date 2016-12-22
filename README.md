# Tracker
Keep track of the time you spend on tasks

## Usage

    tracker --help

## Dev setup

    virtualenv venv
    . venv/bin/activate
    pip install --editable .

### CLI
#### Start tracking a task

    tracker start <task_name>

returns

    <task_name> started at <date/time>

#### Stop tracking current task

    tracker stop

returns

    <task_name> stopped
        Time: <start_time> -- <stop_time>
    Duration: <time>

OR

    No currently running task

#### Show state of currently tracked task

    tracker status

returns

    Running task: <task_name>
         Started: <date/time>
        Duration: <time>

OR

    No currently running task

#### Show history of tasks -- today is default

    tracker burndown

returns

    -- <task_name>
      Total Duration: 4 hours, 16 minutes
      Sessions:
        12:34 - 03:14 PM EST
        04:00 - 04:30 PM EST

    -- <task_name>
      Total Duration: 30 minutes
      Sessions:
        08:15 - 08:30 AM EST
