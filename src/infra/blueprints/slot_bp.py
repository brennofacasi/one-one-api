from flask_openapi3 import Tag, APIBlueprint

from src.infra.schemas import SlotSearchById, SuccessSchema, ErrorSchema
from src.infra.repositories import DBSlotRepository, DBMentorRepository
from src.usecases.slot import DeleteSlot


slot_tag = Tag(
    name="Horários", description="Adição, visualização, atualização de horários.")

slot_blueprint = APIBlueprint(
    "slot", __name__, url_prefix="/slot", abp_tags=[slot_tag])


@slot_blueprint.delete("/<string:id>", responses={"200": SuccessSchema, "400": ErrorSchema})
def delete_slot(path: SlotSearchById):
    slot_repository = DBSlotRepository()

    try:
        DeleteSlot(slot_repository).execute(path.id)
        return {"message": "Slot deleted."}, 200

    except Exception as e:
        return {"message": str(e)}, 400
