from .errors import MeetingNotFoundError


class DeleteMeeting:
    def __init__(self, meeting_repository, slot_repository):
        self.meeting_repository = meeting_repository
        self.slot_repository = slot_repository

    def execute(self, meeting_id):
        meeting_repository = self.meeting_repository
        slot_repository = self.slot_repository

        if meeting_repository.find_by_id(meeting_id) is None:
            raise MeetingNotFoundError

        slots = slot_repository.find_by_meeting_id(meeting_id)

        for slot in slots:
            slot_repository.delete(slot.id)

        meeting_repository.delete(meeting_id)
