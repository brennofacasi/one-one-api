
from src.entities import Mentor, Mentee, Meeting
from tests.repositories.fake_generate_services import FakeGenerate
from tests.repositories.in_memory_meeting_repository import InMemoryMeetingRepository
from src.usecases.meeting import CreateMeeting


def test_create_meeting():
    meeting_repository = InMemoryMeetingRepository()
    generator = FakeGenerate()
    mentor = Mentor('João', 'Moura', 'joao@email.com', 2)
    mentee = Mentee('Ana', 'Ribeiro', 'ana@email.com', 'Nouhau', 3)
    meeting = Meeting(
        mentor.id, mentee.id, '2023-09-09 19:01:38.232448', 30, 'ONLINE')
    id = CreateMeeting(meeting_repository, generator).execute(meeting)
    assert meeting_repository.find_by_id(id).mentor_id == mentor.id
