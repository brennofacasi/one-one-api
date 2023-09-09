class History:
    def __init__(self, meeting, status, created_at):
        self.meeting = meeting
        self.status = status
        self.created_at = created_at

    def done(self):
        self.status = 'DONE'

    def rescheduled(self):
        self.status = 'RESCHEDULED'

    def cancelled(self):
        self.status = 'CANCELLED'
