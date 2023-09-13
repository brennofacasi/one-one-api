
from src.entities import Mentor, Meeting
from tests.repositories.fake_generate_services import FakeGenerate
from tests.repositories.in_memory_meeting_repository import InMemoryMeetingRepository
from tests.repositories.in_memory_mentor_repository import InMemoryMentorRepository
from tests.repositories.in_memory_mentee_repository import InMemoryMenteeRepository

from src.usecases.meeting import CreateMeeting, DeleteMeeting


def test_create_meeting():
    meeting_repository = InMemoryMeetingRepository()
    mentor_repository = InMemoryMentorRepository()
    mentee_repository = InMemoryMenteeRepository()
    generator = FakeGenerate()

    mentor = Mentor('João', 'Moura', 'joao@email.com', 2)
    mentor_repository.add(mentor)

    mentee_id = 3

    meeting = Meeting(
        mentor.id, mentee_id, '2023-09-09 19:01:38.232448', 30, 'ONLINE')

    id = CreateMeeting(meeting_repository, mentor_repository,
                       mentee_repository, generator).execute(meeting)

    DeleteMeeting(meeting_repository).execute(id)

    assert meeting_repository.find_by_id(id) == None
