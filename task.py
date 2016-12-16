class Task(object):
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None

    def to_csv(self):
        return "{name},{start_date},{end_date}".format(self.__dict__)
