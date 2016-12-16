import os


class Store(object):
    def __init__(self, file):
        self.file = file

    def insert(self, task):
        """Creates a new task record"""
        with open(self.file, "a") as f:
            f.write(task.to_csv())

    def delete(self):
        """Deletes entire store file"""
        if os.path.exists(self.file):
            os.remove(self.file)
