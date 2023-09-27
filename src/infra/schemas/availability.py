from datetime import datetime, time
from pydantic import BaseModel
from typing import List, Optional


class AvailabilitySchema(BaseModel):
    mentor_id: int = 1
    week_day: int = 0
    from_time: time = "10:00:00"
    to_time: time = "15:00:00"


class AvailabilityCreateSchema(BaseModel):
    availabilities: List[AvailabilitySchema]


class AvailabilityViewSchema(BaseModel):
    id: int
    mentor_id: int
    week_day: int
    from_time: time
    to_time: time
    created_at: datetime
    updated_at: datetime


class AvailabilityListSchema(BaseModel):
    availabilities: List[AvailabilityViewSchema]


class AvailabilitySearchById(BaseModel):
    id: Optional[int] = None


class AvailabilitySearchByMentorId(BaseModel):
    mentor_id: Optional[int] = None


def show_availabilities(availabilities: List[AvailabilityViewSchema]):
    week_days = ("segunda-feira", "terça-feira", "quarta-feira",
                 "quinta-feira", "sexta-feira", "sábado", "domingo")
    result = []
    for availability in availabilities:
        week_day = week_days[availability.week_day]
        result.append({
            "id": availability.id,
            "mentor_id": availability.mentor_id,
            "week_day": week_day,
            "from_time": str(availability.from_time),
            "to_time": str(availability.to_time),
            "created_at": availability.created_at,
            "updated_at": availability.updated_at
        })
    return {"availabilities": result}
