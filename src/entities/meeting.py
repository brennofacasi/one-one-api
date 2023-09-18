
class Meeting:
    def __init__(self, mentor_id, mentee_id, slot_id, kind, id=None):
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id
        self.slot_id = slot_id
        self.kind = kind
        self.id = id

    def set_id(self, id):
        self.id = id
