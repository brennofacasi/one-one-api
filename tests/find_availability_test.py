from tests.repositories.in_memory_availability_repository import InMemoryAvailabilityRepository


def test_find_availability_in_memory():
    availability_repository = InMemoryAvailabilityRepository()
    found_availability = availability_repository.find_by_mentor_id(5)
    assert len(found_availability) == 4
