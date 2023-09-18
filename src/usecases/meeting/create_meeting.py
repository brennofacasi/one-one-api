from src.entities import Meeting
from src.usecases.ports import MeetingRepository, MentorRepository, MenteeRepository, SlotRepository, GenerateServices
from .errors import MentorDoesNotExistError, MenteeDoesNotExistError, SlotUnavailable


class CreateMeeting:
    """Build a new :class:`CreateMeeting`.

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
        self.meeting_id = generator.id()

    def execute(self, meeting: Meeting):
        """
        It executes the creation of a meeting. It requires the ```meeting``` object.
        """

        # Set repositories
        mentor_repository = self.mentor_repository
        mentee_repository = self.mentee_repository
        meeting_repository = self.meeting_repository
        slot_repository = self.slot_repository

        # Check if mentor exists
        if mentor_repository.find_by_id(meeting.mentor_id) is None:
            raise MentorDoesNotExistError()

        # Check if mentee exists
        if mentee_repository.find_by_id(meeting.mentee_id) is None:
            raise MenteeDoesNotExistError()

        # Check if slot is available
        required_slot = slot_repository.find_by_id(meeting.slot_id)
        if required_slot.is_available is False:
            raise SlotUnavailable

        # Set an id to meeting
        meeting.set_id(self.meeting_id)

        # Put in database
        meeting_repository.add(meeting)

        # Make slot unavailable
        slot_repository.set_unavailable_by_id(meeting.slot_id)

        # Return id
        return meeting.id
