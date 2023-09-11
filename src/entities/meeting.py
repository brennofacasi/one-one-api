import uuid


class Meeting:
    def __init__(self, mentor, mentee, date, duration, kind, id=uuid.uuid1()):
        self.id = id
        self.mentor = mentor
        self.mentee = mentee
        self.date = date
        self.duration = duration
        self.kind = kind
