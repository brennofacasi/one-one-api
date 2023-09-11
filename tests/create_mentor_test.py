from src.usecases.mentor import CreateMentor
from .repositories.in_memory_mentor_repository import InMemoryMentorRepository


def test_create_mentor_in_memory():
    mentor_repository = InMemoryMentorRepository()
    first_name = 'Brenno'
    last_name = 'Cavalcante'
    email = 'brenno@nouhau.pro'
    CreateMentor(mentor_repository).execute(first_name, last_name, email)
    assert mentor_repository.find_by_email(email).email == email
