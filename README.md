# Tracker
Keep track of the time you spend on tasks

## Usage

    tracker --help

## Dev setup

    . venv/bin/activate
    pip install --editable .

### CLI
#### Start tracking a task

    tracker start <job_name>

returns

    <job_name> started at <date/time>

#### Stop tracking current task

    tracker stop

returns

    <job_name> stopped
        Time: <start_time> -- <stop_time>
    Duration: <time>

#### Show state of currently tracked task

    tracker status

returns

    Running task: <job_name>
    Started: <date/time>
    Duration: <time>

OR

    No currently running task

