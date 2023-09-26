from flask_openapi3 import Tag, APIBlueprint

from src.entities import Availability
from src.usecases.availability import CreateAvailabilities, GetAvailabilities, GetMentorAvailabilities, DeleteAvailability

from src.infra.schemas import AvailabilityCreateSchema, SuccessSchema, AvailabilityListSchema, AvailabilitySearchByMentorId, ErrorSchema, AvailabilitySearchById, show_availabilities
from src.infra.repositories import DBAvailabilityRepository
from src.usecases.availability.errors import AvailabilityNotFoundError

availability_tag = Tag(
    name="Disponibilidade", description="Adição, visualização e deleção de dias de disponibilidade dos mentores.")

availability_blueprint = APIBlueprint(
    "availability", __name__, url_prefix="/availability", abp_tags=[availability_tag])


@availability_blueprint.get("/", responses={"200": AvailabilityListSchema, "400": ErrorSchema})
def get_availabilities(query: AvailabilitySearchByMentorId):
    """
    Mostra todas as disponibilidades do banco de dados.

    Faz a pesquisa das disponibilidades pelo ID do mentor.
    """

    repository = DBAvailabilityRepository()

    try:
        if query.mentor_id is not None:
            result = GetMentorAvailabilities(
                repository).execute(query.mentor_id)
            return show_availabilities(result)

        result = GetAvailabilities(repository).execute()
        return show_availabilities(result)

    except Exception as e:
        return {"message": str(e)}, 400


@availability_blueprint.post("/", responses={"200": SuccessSchema})
def add_availabilities(body: AvailabilityCreateSchema):
    """
    Adiciona disponibilidades ao banco de dados.

    Cria no repositório disponibilidade por semana, com intervalo de horas.
    """
    repository = DBAvailabilityRepository()
    availabilities = []

    for availability in body.availabilities:
        availabilities.append(Availability(
            availability.mentor_id, availability.week_day, availability.from_time, availability.to_time))

    CreateAvailabilities(repository).execute(availabilities)
    return {"message": "Availabilities added."}


@availability_blueprint.delete("/<int:id>", responses={"200": SuccessSchema, "400": ErrorSchema, "404": ErrorSchema})
def delete_availability(path: AvailabilitySearchById):
    """
    Deleta disponibilidade do banco de dados.

    Realiza a deleção da disponibilidade pelo id. Retorna mensagem de sucesso.
    """
    repository = DBAvailabilityRepository()

    try:
        DeleteAvailability(repository).execute(path.id)
        return {
            "id": path.id,
            "message": "Availability deleted."
        }, 200

    except AvailabilityNotFoundError as e:
        return {"message": str(e)}, 404

    except Exception as e:
        return {"message": str(e)}, 400
