from pydantic import BaseModel
from datetime import time


class AvailabilitySchema(BaseModel):
    mentor_id: int = 1
    week_day: int = 0
    from_time: time = "10:00:00"
    to_time: time = "15:00:00"


class AvailabilityCreateSchema(BaseModel):
    availabilities: list[AvailabilitySchema]
