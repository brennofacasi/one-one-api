from pydantic import BaseModel
from datetime import datetime
from typing import List


class AvailabilitySchema(BaseModel):
    mentor_id: int
    week_day: int
    from_time: datetime
    to_time: datetime
