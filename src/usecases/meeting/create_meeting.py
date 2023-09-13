from src.entities import Meeting
from src.usecases.ports import MeetingRepository, MentorRepository, MenteeRepository, GenerateServices
from .errors import MentorDoesNotExistError, MenteeDoesNotExistError


class CreateMeeting:
    '''Construct a new :class:`CreateMeeting`.

    It is used to create a new meeting in the repository.
    The class requires two arguments:

    `meeting_repository` The repository class.

    `generator` The generator class, used to create ids and other utils.

    '''

    def __init__(self, meeting_repository: MeetingRepository, mentor_repository: MentorRepository, mentee_repository: MenteeRepository, generator: GenerateServices):
        self.meeting_repository = meeting_repository
        self.mentor_repository = mentor_repository
        self.mentee_repository = mentee_repository

        self.generator = generator
        self.id = generator.id()

    def execute(self, meeting: Meeting):
        '''
        It executes the creation of a meeting. It requires the ```meeting``` object.
        '''
        mentor_repository = self.mentor_repository
        mentee_repository = self.mentee_repository

        if mentor_repository.find_by_id(meeting.mentor_id) == None:
            raise MentorDoesNotExistError()

        if mentee_repository.find_by_id(meeting.mentee_id) == None:
            raise MenteeDoesNotExistError()

        id = self.id
        meeting_repository = self.meeting_repository
        content = Meeting(meeting.mentor_id, meeting.mentee_id,
                          meeting.date, meeting.duration, meeting.kind, id)

        meeting_repository.add(content)
        return id
