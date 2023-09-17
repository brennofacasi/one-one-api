from src.usecases.ports import MinuteRepository


class InMemoryMinuteRepository(MinuteRepository):
    def __init__(self):
        self.minute_list = []

    def add(self, minute):
        self.minute_list.append(minute)

    def find_by_meeting_id(self, meeting_id):
        for minute in self.minute_list:
            if minute.meeting.id == meeting_id:
                return minute
