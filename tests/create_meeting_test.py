import uuid
from src.entities import Mentor, Mentee
from tests.repositories.in_memory_meeting_repository import InMemoryMeetingRepository
from src.usecases.meeting import CreateMeeting


def test_create_meeting():
    meeting_repository = InMemoryMeetingRepository()
    id = uuid.uuid1()
    mentor = Mentor('João', 'Moura', 'joao@email.com')
    mentee = Mentee('Ana', 'Ribeiro', 'ana@email.com', 'Nouhau')
    date = '2023-09-09 19:01:38.232448'
    duration = 30
    kind = 'ONLINE'
    CreateMeeting(meeting_repository).perform(
        id, mentor, mentee, date, duration, kind)
    assert meeting_repository.find_by_id(id).mentor == mentor
