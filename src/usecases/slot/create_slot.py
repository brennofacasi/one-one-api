from src.entities import Slot
from src.usecases.ports import SlotRepository, GenerateServices


class CreateSlot:
    def __init__(self, generate_service: GenerateServices, slot_repository: SlotRepository):
        self.slot_repository = slot_repository
        self.generate = generate_service

    def execute(self, slot: Slot):
        slot_id = self.generate.id()
        slot.set_id(slot_id)
        self.slot_repository.add(slot)
