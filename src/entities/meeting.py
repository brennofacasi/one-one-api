
class Meeting:
    def __init__(self, mentor, mentee, date, duration, kind, id=None):
        self.id = id
        self.mentor = mentor
        self.mentee = mentee
        self.date = date
        self.duration = duration
        self.kind = kind
