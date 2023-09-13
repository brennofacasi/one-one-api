
class Meeting:
    def __init__(self, mentor_id, mentee_id, date, duration, kind, id=None):
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id
        self.date = date
        self.duration = duration
        self.kind = kind
        self.id = id
