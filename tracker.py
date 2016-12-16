class Tracker(object):
    def __init__(self, task, store):
        self.store = store
        self.task = task

    def start(self):
        """Records a new task in the store"""
        self.store.insert(self.task)
