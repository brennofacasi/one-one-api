from src.entities import Mentor, Mentee, Minute
from tests.repositories.in_memory_meeting_repository import InMemoryMeetingRepository
from src.usecases.meeting.create_meeting import CreateMeeting


def test_create_meeting_in_repository():
    meeting_repository = InMemoryMeetingRepository()
    id = '2389hd290'
    mentor = Mentor('Brenno', 'brenno@nouhau.pro')
    mentee = Mentee('Talyta', 'talyta@nouhau.pro', 'Nouhau')
    date = '2023-09-09 19:01:38.232448'
    duration = 30
    kind = 'ONLINE'
    minute = Minute(
        'This meeting was very productive and had amazing results.')
    CreateMeeting(meeting_repository).perform(
        id, mentor, mentee, date, duration, kind, minute)
    assert meeting_repository.find_by_id(id).mentor == mentor
