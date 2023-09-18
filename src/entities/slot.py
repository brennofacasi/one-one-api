class Slot:
    def __init__(self, mentor_id, start_time, end_time, is_available=True, id=None):
        self.mentor_id = mentor_id
        self.start_time = start_time
        self.end_time = end_time
        self.is_available = is_available
        self.id = id

    def set_id(self, id):
        self.id = id
