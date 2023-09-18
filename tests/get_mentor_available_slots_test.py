from tests.repositories.in_memory_availability_repository import InMemoryAvailabilityRepository
from tests.repositories.in_memory_slot_repository import InMemorySlotRepository
from src.usecases.mentor import GetMentorAvailableSlots

import datetime as dt


def test_get_mentor_available_slots_in_memory():
    availability_repository = InMemoryAvailabilityRepository()
    slot_repository = InMemorySlotRepository()
    mentor_id = 5
    result = GetMentorAvailableSlots(mentor_id, dt.datetime(2023, 9, 18), dt.datetime(
        2023, 9, 20), 30, availability_repository, slot_repository).perform()
    # 12 slots, minus 2 unavailable
    assert len(result) == 10
