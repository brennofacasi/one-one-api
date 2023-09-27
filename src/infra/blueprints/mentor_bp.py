from flask_openapi3 import Tag, APIBlueprint
from src.entities import Mentor

from src.infra.repositories import DBMentorRepository, DBAvailabilityRepository, DBSlotRepository
from src.infra.schemas import ErrorSchema, SuccessSchema
from src.infra.schemas.mentor import *

from src.usecases.mentor import *
from src.usecases.mentor.errors import DuplicateMentorError


mentor_tag = Tag(
    name="Mentores", description="Adição, visualização e deleção de mentores.")

mentor_blueprint = APIBlueprint(
    "mentor", __name__, url_prefix="/mentor", abp_tags=[mentor_tag])


@mentor_blueprint.get("/", responses={"200": MentorListSchema,
                                      "400": ErrorSchema, "404": ErrorSchema})
def get_mentors():
    """
    Mostra todos os mentores.

    Retorna uma lista representativa com todos os mentores cadastrados no banco de dados.
    """
    try:
        repository = DBMentorRepository()
        result = GetMentors(repository).execute()

        if not result:
            return {"message": "No mentors found. Add a new one!"}, 404
        else:
            return show_mentors(result)

    except Exception as e:
        return {"message": str(e)}, 400


@mentor_blueprint.post("/", responses={"200": SuccessSchema, "400": ErrorSchema})
def add_mentor(body: MentorSchema):
    """
    Adiciona mentor ao banco de dados.

    Retorna mensagem de sucesso.
    """
    repository = DBMentorRepository()
    try:
        mentor = Mentor(body.first_name, body.last_name, body.email)
        CreateMentor(repository).execute(mentor)
        return {"message": "Mentor added successfully."}, 200

    except DuplicateMentorError as e:
        return {"message": str(e)}, 400


@mentor_blueprint.patch("/", responses={"200": SuccessSchema, "400": ErrorSchema})
def update_mentor(body: MentorEditSchema):
    """
    Atualiza mentor no banco de dados.

    O ID é obrigatório. Retorna mensagem de sucesso.
    """
    try:
        repository = DBMentorRepository()
        EditMentor(repository).execute(body)
        return {"message": "Mentor updated"}, 200
    except Exception as e:
        return {"message": str(e)}, 400


@mentor_blueprint.delete("/<string:id>", responses={"200": SuccessSchema, "400": ErrorSchema})
def delete_mentor(path: MentorSearchById):
    """
    Deleta mentor do banco de dados.

    Realiza a deleção do mentor pelo ID. Retorna mensagem de sucesso.
    """
    repository = DBMentorRepository()
    try:
        DeleteMentor(repository).execute(path.id)
        return {"message": "Mentor deleted."}, 200

    except Exception as e:
        return {"message": str(e)}, 400


@mentor_blueprint.get("/slots")
def get_mentor_available_slots(query: MentorGetAvailableSlotsSchema):
    """
    Gera slots disponíveis do mentor.

    Retorna todos os intervalos de tempo disponíveis em um período de tempo, de acordo com a disponibilidade registrada do mentor, para marcação de reuniões de mentoria.
    """
    availability_repository = DBAvailabilityRepository()
    slot_repository = DBSlotRepository()

    result = GetMentorAvailableSlots(availability_repository, slot_repository).execute(query.mentor_id, query.week_starts,
                                                                                       query.week_ends, query.slot_duration)

    return show_mentor_slots(result)
