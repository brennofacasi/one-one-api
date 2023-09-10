from enum import Enum


class Status(Enum):
    SCHEDULED = 'SCHEDULED'
    RESCHEDULED = 'RESCHEDULED'
    CANCELLED = 'CANCELLED'
    DONE = 'DONE'
