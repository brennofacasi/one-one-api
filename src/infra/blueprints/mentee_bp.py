from flask_openapi3 import Tag, APIBlueprint
from src.infra.schemas import MenteeViewSchema
from src.infra.repositories import ApiMenteeRepository
from src.usecases.mentees import GetMentees

mentee_blueprint = APIBlueprint('mentee', __name__, url_prefix='/mentee')

mentee_tag = Tag(name='Mentodaros',
                 description='Adição, visualização e atualização de usuários mentorados.')


@mentee_blueprint.get('/', tags=[mentee_tag], responses={'200': MenteeViewSchema})
def get_mentees():
    '''
    Mostra usuários mentorados a partir de API Externa

    Retorna representação da listagem de todos os usuários que podem participar de mentorias.
    '''
    repository = ApiMenteeRepository()
    result = GetMentees(repository).execute()
    return result
