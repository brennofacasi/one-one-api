from src.usecases.ports import MinuteRepository


class InMemoryMinuteRepository(MinuteRepository):
    def __init__(self):
        self.minuteList = []

    def add(self, minute):
        self.minuteList.append(minute)

    def find_by_meeting_id(self, meeting_id):
        for minute in self.minuteList:
            if minute.meeting.id == meeting_id:
                return minute
