class SlotUnavailable(Exception):
    def __init__(self):
        message = 'This slot is currently taken.'
        super().__init__(message)
