from src.entities import Slot


class DeleteSlot:
    def __init__(self, slot_repository):
        self.slot_repository = slot_repository

    def execute(self, slot_id):
        repository = self.slot_repository
        repository.delete(slot_id)
