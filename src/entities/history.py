class History:
    def __init__(self, meeting, created_at, motive, status='SCHEDULED'):
        self.meeting = meeting
        self.created_at = created_at
        self.motive = motive
        self.status = status
