import unittest
from store import Store
from task import Task
from tracker import Tracker


class TestTracker(unittest.TestCase):
    def setUp(self):
        self.task = Task("test_task")
        self.store = Store(file="task_store_test.csv")
        self.tracker = Tracker(self.task, store=self.store)
        self.store.delete()

    def test_starting_a_new_task_persists_it_to_the_store(self):
        self.tracker.start()
        with open(self.store.file) as f:
            tasks = f.read()
        self.assertEqual(len(tasks), 1)

    def test_starting_a_new_task_returns_the_started_task(self):
        task = self.tracker.start()
        self.assertTrue(task.start_date)


if __name__ == "__main__":
    unittest.main()
