class MenteeDoesNotExistError(Exception):
    def __init__(self):
        message = 'This mentee does not exist.'
        super().__init__(message)
