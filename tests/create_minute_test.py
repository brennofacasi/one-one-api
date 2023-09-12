from src.entities import Mentor, Mentee, Meeting
from src.usecases.minute import CreateMinute
from tests.repositories.in_memory_minute_repository import InMemoryMinuteRepository


def test_create_minute_in_memory():
    minute_repository = InMemoryMinuteRepository()
    content = 'This is a minute about what was discussed in the meeting.'
    mentor = Mentor('João', 'Moura', 'joao@email.com')
    mentee = Mentee('Ana', 'Ribeiro', 'ana@email.com', 'Nouhau')
    date = '2023-09-09 19:01:38.232448'
    duration = 30
    kind = 'ONLINE'
    meeting = Meeting(mentor, mentee, date, duration, kind)

    CreateMinute(minute_repository).execute(meeting, content)

    assert minute_repository.find_by_meeting_id(
        meeting.id).content == content
