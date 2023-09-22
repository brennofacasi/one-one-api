from src.entities import Meeting, Slot
from src.usecases.ports import *
from .errors import *


class CreateMeeting:
    """
    Build a new :class:`CreateMeeting`.

    It creates a new meeting in the repository.
    """

    def __init__(self,
                 meeting_repository: MeetingRepository,
                 mentor_repository: MentorRepository,
                 mentee_repository: MenteeRepository,
                 slot_repository: SlotRepository,
                 generator: GenerateServices):

        self.meeting_repository = meeting_repository
        self.mentor_repository = mentor_repository
        self.mentee_repository = mentee_repository
        self.slot_repository = slot_repository

        self.generator = generator

    def __periods_overlap(self, period1, period2):
        start1, end1 = period1
        start2, end2 = period2
        return end1 >= start2 and end2 >= start1

    def execute(self, meeting: Meeting):
        """
        It executes the creation of a meeting. It requires the ```meeting``` object.
        """

        # Set repositories
        mentor_repository = self.mentor_repository
        mentee_repository = self.mentee_repository
        meeting_repository = self.meeting_repository
        slot_repository = self.slot_repository

        required_slot = (meeting.slot.start_time, meeting.slot.end_time)

        # Check if mentor exists
        if mentor_repository.find_by_id(meeting.mentor_id) is None:
            raise MentorDoesNotExistError()

        # Check if mentee exists
        if mentee_repository.find_by_id(meeting.mentee_id) is None:
            raise MenteeDoesNotExistError()

        # Check if slot is available
        mentor_slots = slot_repository.find_by_mentor_id(meeting.mentor_id)

        for mentor_slot in mentor_slots:
            unavailable_slot = (mentor_slot.start_time, mentor_slot.end_time)
            if self.__periods_overlap(required_slot, unavailable_slot):
                raise SlotUnavailable

        # Set ids
        meeting_id = self.generator.id()
        slot_id = self.generator.id()

        meeting.slot.id = slot_id
        meeting.id = meeting_id

        # Put in database
        meeting_repository.add(meeting)
        slot_repository.add(meeting.slot)

        # Return id
        return meeting.id
