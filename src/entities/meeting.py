
class Meeting:
    def __init__(self, mentor_id, mentee_id, slot, kind, id=None):
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id
        self.slot = slot
        self.kind = kind
        self.id = id
