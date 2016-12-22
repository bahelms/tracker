from datetime import datetime


class Tracker(object):
    def __init__(self, task, store):
        """
        Args:
            task (:obj:`Task`): the task to be tracked
            store (:obj:`Store`): handles specifics of task persistence
        """
        self.store = store
        self.task = task
        self.time_format = "%m/%d/%y %I:%M %p %Z"

    def start(self):
        """Records a new task in the store

        Returns:
            (:obj:`Task`): the task object
        """
        self.task.start_date = datetime.today().strftime(self.time_format)
        self.store.insert(self.task)
        return self.task
