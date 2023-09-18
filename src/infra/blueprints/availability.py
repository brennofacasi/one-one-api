from flask_openapi3 import Tag, APIBlueprint


availability_tag = Tag(
    name="Disponibilidade", description="Adição, visualização, atualização e deleção de dias de disponibilidade dos mentores.")

availability_blueprint = APIBlueprint(
    "availability", __name__, url_prefix="/availability", abp_tags=[availability_tag])

# @availability_blueprint.post("/")
# def add_availability(body):
