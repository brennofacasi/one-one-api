class MentorDoesNotExistError(Exception):
    def __init__(self):
        message = 'This mentor does not exist.'
        super().__init__(message)
