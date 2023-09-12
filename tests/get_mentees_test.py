from tests.repositories.in_memory_mentee_repository import InMemoryMenteeRepository
from src.usecases.mentees import GetMentees


def test_get_mentees_in_memory():
    mentees_repository = InMemoryMenteeRepository()
    usecase = GetMentees(mentees_repository)
    mentees = usecase.execute()
    assert len(mentees) == 5
