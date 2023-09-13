from src.usecases.ports import MeetingRepository
from src.usecases.meeting.errors import MeetingNotFoundError


class DeleteMeeting:
    def __init__(self, meeting_repository: MeetingRepository):
        self.meeting_repository = meeting_repository

    def execute(self, meeting_id):
        repository = self.meeting_repository
        if repository.find_by_id(meeting_id) == None:
            raise MeetingNotFoundError()

        repository.delete(meeting_id)
