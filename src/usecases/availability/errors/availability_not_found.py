class AvailabilityNotFoundError(Exception):
    def __init__(self):
        message = 'Availability not found.'
        super().__init__(message)
