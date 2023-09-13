import random
from src.infra.services import Generate


class FakeGenerate(Generate):
    def id(self):
        generatedId = f"id_{random.randint(5, 200)}"
        return generatedId
