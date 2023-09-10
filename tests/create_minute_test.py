import uuid
from src.entities import Mentor, Mentee, Meeting
from src.usecases.minute import CreateMinute
from tests.repositories.in_memory_minute_repository import InMemoryMinuteRepository


def test_create_minute():
    minute_repository = InMemoryMinuteRepository()
    content = 'This is a minute about what was discussed in the meeting.'
    id = uuid.uuid1()
    mentor = Mentor('Brenno', 'brenno@nouhau.pro')
    mentee = Mentee('Talyta', 'talyta@nouhau.pro', 'Nouhau')
    date = '2023-09-09 19:01:38.232448'
    duration = 30
    kind = 'ONLINE'
    meeting = Meeting(id, mentor, mentee, date, duration, kind)

    CreateMinute(minute_repository).perform(meeting, content)

    assert minute_repository.find_by_meeting_id(
        id).content == content
