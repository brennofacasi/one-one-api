class Slot:
    def __init__(self, mentor_id, start_time, end_time, meeting_id=None):
        self.mentor_id = mentor_id
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_id = meeting_id
