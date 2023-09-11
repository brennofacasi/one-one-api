class DuplicateMentorError(Exception):
    def __init__(self):
        message = 'This mentor already exists.'
        super().__init__(message)
