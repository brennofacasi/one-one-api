from nanoid import generate
from src.usecases.ports import GenerateServices


class Generate(GenerateServices):

    def id(self):
        nano_id = generate('123456789abcdefghijklmnopqrstuvwxyz-', 12)
        return nano_id
