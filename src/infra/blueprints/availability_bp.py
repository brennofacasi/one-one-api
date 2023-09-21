from flask_openapi3 import Tag, APIBlueprint

from src.entities import Availability
from src.usecases.availability import CreateAvailabilities

from src.infra.schemas import AvailabilityCreateSchema, SuccessSchema
from src.infra.repositories import DBAvailabilityRepository


availability_tag = Tag(
    name="Disponibilidade", description="Adição, visualização, atualização e deleção de dias de disponibilidade dos mentores.")

availability_blueprint = APIBlueprint(
    "availability", __name__, url_prefix="/availability", abp_tags=[availability_tag])


@availability_blueprint.post("/", responses={"200": SuccessSchema})
def add_availability(body: AvailabilityCreateSchema):
    repository = DBAvailabilityRepository()
    availabilities = []

    for availability in body.availabilities:
        availabilities.append(Availability(
            availability.mentor_id, availability.week_day, availability.from_time, availability.to_time))

    CreateAvailabilities(repository).execute(availabilities)
    return {"message": "Availabilities added."}
