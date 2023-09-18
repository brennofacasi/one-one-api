from flask_cors import CORS
from flask import redirect
from flask_openapi3 import Info, OpenAPI, Tag
from src.infra.blueprints import meeting_blueprint, mentor_blueprint, mentee_blueprint, slot_blueprint

info = Info(title="Mementor Api",
            description="Aplicação para agendamento de reuniões de mentorias.", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# Tags
home_tag = Tag(name="Home", description="Rota para Swagger.")


@app.get("/", tags=[home_tag])
def home():
    return redirect("/openapi/swagger")


# Register Blueprints
app.register_api(meeting_blueprint)
app.register_api(mentor_blueprint)
app.register_api(mentee_blueprint)
app.register_api(slot_blueprint)
