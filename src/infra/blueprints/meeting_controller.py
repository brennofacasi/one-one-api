from flask import jsonify
from flask_openapi3 import Tag, APIBlueprint
from src.infra.schemas.meeting import MeetingViewSchema, MeetingSchema
from src.usecases.meeting import CreateMeeting
from src.infra.repositories import FlaskMeetingRepository

meeting_blueprint = APIBlueprint('meeting', __name__, url_prefix='/meeting')

meeting_tag = Tag(
    name='Meetings', description='Adição, visualização e atualização de reuniões.')


@meeting_blueprint.get('/', tags=[meeting_tag], responses={"200": MeetingViewSchema})
def get_meetings():
    # TO DO - Implementar
    return 'Deu certo'


@meeting_blueprint.post('/', tags=[meeting_tag])
def add_meeting(body: MeetingSchema):
    CreateMeeting(FlaskMeetingRepository).execute(body.mentor_id,
                                                  body.mentee_id, body.date, body.duration, body.kind)
