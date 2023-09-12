from flask_openapi3 import Tag, APIBlueprint
from src.infra.repositories import DBMentorRepository
from src.infra.schemas import MentorSchema

from src.usecases.mentor import CreateMentor
from src.usecases.mentor.errors import DuplicateMentorError

mentor_blueprint = APIBlueprint('mentor', __name__, url_prefix='/mentor')

mentor_tag = Tag(
    name='Mentores', description='Adição, visualização e atualização de mentores.')


@mentor_blueprint.get('/', tags=[mentor_tag])
def get_mentors():
    # TO DO - Implementar
    return 'Listar mentores'


@mentor_blueprint.post('/', tags=[mentor_tag])
def add_mentor(body: MentorSchema):
    repository = DBMentorRepository()
    try:
        CreateMentor(repository).execute(body)
        return {"message": "Mentor added successfully."}, 200

    except DuplicateMentorError as e:
        return {"message": "Mentor already exists."}, 400
