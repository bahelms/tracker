class Task(object):
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None

    def to_csv(self):
        """Format: task_name,start_date,end_date

        Returns:
            (str): a csv representation of a Task
        """
        return "{name},{start_date},{end_date}\n".format(**self.__dict__)
