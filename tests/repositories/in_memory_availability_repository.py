from src.entities import Availability
from src.usecases.ports import AvailabilityRepository

import datetime as dt


class InMemoryAvailabilityRepository(AvailabilityRepository):
    def __init__(self):
        self.available_list = [
            Availability(5, 0, "09:00:00", "11:00:00"),  # 4
            Availability(5, 1, "09:00:00", "11:00:00"),  # 4
            Availability(5, 2, "09:00:00", "11:00:00"),  # 4 = 12
            Availability(5, 4, "10:00:00", "11:00:00"),
            Availability(6, 1, "10:00:00", "12:00:00"),
            Availability(6, 2, "09:00:00", "12:00:00"),
        ]

    def add(self, availability):
        self.available_list.append(availability)

    def find_by_mentor_id(self, mentor_id):
        result = []
        for availability in self.available_list:
            if availability.mentor_id == mentor_id:
                result.append(availability)
        return result
