from nanoid import generate
from src.entities import Mentor, Mentee, Meeting
from tests.repositories.in_memory_meeting_repository import InMemoryMeetingRepository
from src.usecases.meeting import CreateMeeting


def test_create_meeting():
    meeting_repository = InMemoryMeetingRepository()
    mentor = Mentor('João', 'Moura', 'joao@email.com')
    mentee = Mentee('Ana', 'Ribeiro', 'ana@email.com', 'Nouhau')
    meeting = Meeting(
        mentor, mentee, '2023-09-09 19:01:38.232448', 30, 'ONLINE')
    id = CreateMeeting(meeting_repository).execute(
        meeting)
    assert meeting_repository.find_by_id(id).mentor == mentor
