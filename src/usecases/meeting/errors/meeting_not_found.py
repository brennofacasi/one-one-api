class MeetingNotFoundError(Exception):
    def __init__(self):
        message = 'Meeting not found.'
        super().__init__(message)
