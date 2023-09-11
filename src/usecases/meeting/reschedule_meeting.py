from datetime import datetime
from src.entities import History, Status


class RescheduleMeeting:
    def __init__(self, history_repository):
        self.history_repository = history_repository

    def execute(self, meeting):
        repository = self.history_repository
        now = datetime.now()
        history = History(meeting.id, now, Status.RESCHEDULED)
        repository.add(history)
