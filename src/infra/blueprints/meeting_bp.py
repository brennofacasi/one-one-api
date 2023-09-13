from flask_openapi3 import Tag, APIBlueprint

from src.usecases.meeting import CreateMeeting, GetMeetings, DeleteMeeting
from src.usecases.meeting.errors import MentorDoesNotExistError, MenteeDoesNotExistError, MeetingNotFoundError

from src.infra.services import Generate
from src.infra.schemas import MeetingViewSchema, MeetingSchema, ErrorSchema, SuccessSchema, MeetingSearchById, show_meetings
from src.infra.repositories import DBMeetingRepository, DBMentorRepository, ApiMenteeRepository

meeting_tag = Tag(
    name='Reuniões', description='Adição, visualização, atualização e deleção de reuniões.')

meeting_blueprint = APIBlueprint(
    'meeting', __name__, url_prefix='/meeting', abp_tags=[meeting_tag])


@meeting_blueprint.get('/', responses={"200": MeetingViewSchema, "404": ErrorSchema})
def get_meetings():
    '''
    Mostra todas as reuniões.

    Retorna representação da listagem de todas as reuniões cadastradas no banco de dados.
    '''
    meeting_repository = DBMeetingRepository()
    mentee_repository = ApiMenteeRepository()

    result = GetMeetings(meeting_repository).execute()
    return show_meetings(result, mentee_repository)


@meeting_blueprint.post('/', responses={"200": SuccessSchema, "400": ErrorSchema})
def add_meeting(body: MeetingSchema):
    '''
    Adiciona reunião ao banco de dados.

    Retorna mensagem de sucesso com o id.
    '''

    meeting_repository = DBMeetingRepository()
    mentor_repository = DBMentorRepository()
    mentee_repository = ApiMenteeRepository()
    generator = Generate()

    try:

        id = CreateMeeting(meeting_repository,
                           mentor_repository, mentee_repository, generator).execute(body)
        return {
            "id": id,
            "message": "Meeting added successfully."
        }, 200

    except MentorDoesNotExistError as e:
        return {
            "message": "This mentor does not exist."
        }, 400

    except MenteeDoesNotExistError as e:
        return {
            "message": "This mentee does not exist."
        }, 400


@meeting_blueprint.delete('/<string:id>', responses={"200": SuccessSchema, "400": ErrorSchema})
def delete_meeting(path: MeetingSearchById):
    '''
    Deleta reunião do bando de dados.

    Realiza a deleção da reunião pelo id. Retorna mensagem de sucesso.
    '''
    meeting_repository = DBMeetingRepository()
    try:

        DeleteMeeting(meeting_repository).execute(path.id)
        return {
            "id": path.id,
            "message": "Meeting deleted."
        }, 200

    except MeetingNotFoundError as e:
        return {
            "message": "Meeting not found."
        }
