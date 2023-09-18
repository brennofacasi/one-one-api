from tests.repositories.in_memory_slot_repository import InMemorySlotRepository


def test_find_mentor_slots_in_memory():
    slots_repository = InMemorySlotRepository()
    found_slots = slots_repository.find_by_mentor_id(5)
    assert len(found_slots) > 1
