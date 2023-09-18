from flask_openapi3 import Tag, APIBlueprint

from src.infra.repositories import DBMentorRepository
from src.infra.schemas import ErrorSchema, SuccessSchema
from src.infra.schemas.mentor import *

from src.usecases.mentor import *
from src.usecases.mentor.errors import DuplicateMentorError

mentor_blueprint = APIBlueprint("mentor", __name__, url_prefix="/mentor")

mentor_tag = Tag(
    name="Mentores", description="Adição, visualização e atualização de mentores.")


@mentor_blueprint.get("/", tags=[mentor_tag], responses={"200": MentorListSchema,
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


@mentor_blueprint.post("/", tags=[mentor_tag], responses={"200": SuccessSchema, "400": ErrorSchema})
def add_mentor(body: MentorSchema):
    """
    Adiciona mentor ao banco de dados.

    Retorna mensagem de sucesso.
    """
    repository = DBMentorRepository()
    try:
        CreateMentor(repository).execute(body)
        return {"message": "Mentor added successfully."}, 200

    except DuplicateMentorError as e:
        return {"message": str(e)}, 400
