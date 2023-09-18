from flask_openapi3 import Tag, APIBlueprint
from src.entities import Slot

from src.infra.schemas import SlotSchema, SlotSearchById
from src.infra.repositories import DBSlotRepository
from src.usecases.slot import CreateSlot

from src.infra.services import Generate


slot_tag = Tag(
    name="Horários", description="Adição, visualização, atualização de horários.")

slot_blueprint = APIBlueprint(
    "slot", __name__, url_prefix="/slot", abp_tags=[slot_tag])


@slot_blueprint.post("/")
def add_slot(body: SlotSchema):
    slot_repository = DBSlotRepository()
    generate_service = Generate()

    slot = Slot(body.mentor_id, body.start_time,
                body.end_time, body.is_available)
    CreateSlot(generate_service, slot_repository).execute(slot)

    return {"message": "Slot criado"}, 200


@slot_blueprint.patch("/<int:id>")
def update_slot(path: SlotSearchById):
    slot_repository = DBSlotRepository()
    slot_repository.set_unavailable_by_id(path.id)

    return {"message": "Foi?"}, 200
