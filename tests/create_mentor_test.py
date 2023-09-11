from src.entities import Mentor
from src.usecases.mentor import CreateMentor
from .repositories.in_memory_mentor_repository import InMemoryMentorRepository


def test_create_mentor_in_memory():
    mentor_repository = InMemoryMentorRepository()
    mentor = Mentor('Brenno', 'Cavalcante', 'brenno@nouhau.pro')
    usecase = CreateMentor(mentor_repository)
    usecase.execute(mentor)
    assert mentor_repository.find_by_email(mentor.email).email == mentor.email
