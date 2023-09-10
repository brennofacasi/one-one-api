from src.usecases.ports import HistoryRepository


class InMemoryHistoryRepository(HistoryRepository):
    def __init__(self):
        self.historyList = []

    def add(self, history):
        self.historyList.append(history)

    def find_by_meeting_id(self, meeting_id):
        for history in self.historyList:
            if history.meeting == meeting_id:
                return history
