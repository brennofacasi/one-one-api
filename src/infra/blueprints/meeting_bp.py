from flask_openapi3 import Tag, APIBlueprint
from src.entities.meeting import Meeting
from src.infra.services import Generate
from src.infra.schemas import ErrorSchema, SuccessSchema

from src.usecases.meeting import *
from src.usecases.meeting.errors import *
from src.infra.schemas.meeting import *
from src.infra.repositories import *

meeting_tag = Tag(
    name="Reuniões", description="Adição, visualização, atualização e deleção de reuniões.")

meeting_blueprint = APIBlueprint(
    "meeting", __name__, url_prefix="/meeting", abp_tags=[meeting_tag])


@meeting_blueprint.get("/", responses={"200": MeetingViewSchema, "404": ErrorSchema})
def get_meetings():
    """
    Mostra todas as reuniões.

    Retorna representação da listagem de todas as reuniões cadastradas no banco de dados.
    """
    meeting_repository = DBMeetingRepository()
    mentee_repository = ApiMenteeRepository()

    result = GetMeetings(meeting_repository).execute()
    return show_meetings(result, mentee_repository)


@meeting_blueprint.post("/", responses={"200": SuccessSchema, "400": ErrorSchema})
def add_meeting(body: MeetingSchema):
    """
    Adiciona reunião ao banco de dados.

    Retorna mensagem de sucesso com o id.
    """

    meeting_repository = DBMeetingRepository()
    mentor_repository = DBMentorRepository()
    mentee_repository = ApiMenteeRepository()
    slot_repository = DBSlotRepository()
    generator = Generate()

    try:
        meeting = Meeting(body.mentor_id, body.mentee_id,
                          body.slot_id, body.kind)
        meeting_id = CreateMeeting(meeting_repository, mentor_repository,
                                   mentee_repository, slot_repository, generator).execute(meeting)
        return {
            "id": meeting_id,
            "message": "Meeting added successfully."
        }, 200

    except MentorDoesNotExistError as e:
        return {"message": str(e)}, 400

    except MenteeDoesNotExistError as e:
        return {"message": str(e)}, 400

    except SlotUnavailable as e:
        return {"message": str(e)}, 400

    except Exception as e:
        print(str(e))
        return {"message": "Oops, there's something wrong."}, 400


@meeting_blueprint.delete("/<string:id>", responses={"200": SuccessSchema, "400": ErrorSchema})
def delete_meeting(path: MeetingSearchById):
    """
    Deleta reunião do bando de dados.

    Realiza a deleção da reunião pelo id. Retorna mensagem de sucesso.
    """
    meeting_repository = DBMeetingRepository()
    try:

        DeleteMeeting(meeting_repository).execute(path.id)
        return {
            "id": path.id,
            "message": "Meeting deleted."
        }, 200

    except MeetingNotFoundError as e:
        return {"message": str(e)}, 404
