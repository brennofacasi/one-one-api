import uuid
from tests.repositories.in_memory_history_repository import InMemoryHistoryRepository
from src.usecases.meeting import RescheduleMeeting
from src.entities import Mentor, Mentee, Meeting, Status


def test_reschedule_meeting():
    history_repository = InMemoryHistoryRepository()
    id = uuid.uuid1()
    mentor = Mentor('João', 'Moura', 'joao@email.com')
    mentee = Mentee('Ana', 'Ribeiro', 'ana@email.com', 'Nouhau')
    date = '2023-09-09 19:01:38.232448'
    duration = 30
    kind = 'ONLINE'
    meeting = Meeting(id, mentor, mentee, date, duration, kind)
    RescheduleMeeting(history_repository).perform(meeting)
    assert history_repository.find_by_meeting_id(
        id).status == Status.RESCHEDULED
