from src.entities import Slot
from src.usecases.ports import SlotRepository
import datetime as dt


class InMemorySlotRepository(SlotRepository):
    def __init__(self):
        self.slot_list = [
            Slot(5, dt.datetime(2023, 9, 18, 9, 30), dt.datetime(
                2023, 9, 18, 10, 00),  "28he29hsj02"),
            Slot(5, dt.datetime(2023, 9, 18, 10, 30), dt.datetime(
                2023, 9, 18, 11, 00),  "whdeh3498h9")
        ]

    def add(self, slot):
        self.slot_list.append(slot)

    def find_by_mentor_id(self, mentor_id):
        result = []
        for slot in self.slot_list:
            if slot.mentor_id == mentor_id:
                result.append(slot)
        return result
