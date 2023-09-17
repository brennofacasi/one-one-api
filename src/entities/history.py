class History:
    def __init__(self, meeting, created_at, motive, status='SCHEDULED', old_date=None, new_date=None):
        self.meeting = meeting
        self.created_at = created_at
        self.motive = motive
        self.status = status
        self.old_date = old_date
        self.new_date = new_date
