from reminders.task import Task
from datetime import date
from freezegun import freeze_time


class TestTask:
    def test_constructor(self):
        task: Task = Task('some name', date(2018, 12, 15), 15)
        assert True

    def test_subject(self):
        task: Task = Task('some name', date(2018, 12, 15), 15,
                          tasks=['joy', 'hell', 'cat'], next_task=2)
        assert task.subject() == 'hell'
        task: Task = Task('some name', date(2018, 12, 15), 15)
        assert task.subject() == 'some name'

    def test_date_due(self):
        task: Task = Task('some name', date(2018, 12, 3), 15)
        assert task.date_due() == date(2018, 12, 18)

    @freeze_time("2018-11-01")
    def test_due(self):
        task: Task = Task('some name', date(2018, 10, 28), 1)
        assert task.due()
        task2: Task = Task('some name', date(2018, 10, 30), 3)
        assert not task2.due()






