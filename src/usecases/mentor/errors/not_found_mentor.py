class NotFoundMentorError(Exception):
    def __init__(self):
        message = 'Mentor not found.'
        super().__init__(message)
