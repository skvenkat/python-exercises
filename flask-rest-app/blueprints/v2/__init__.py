# blueprints/basic_endpoints/__ini__.py
from flask import Blueprint, request

blueprint_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

@blueprint_v2.route('/hello_world')
def hello_world():
    return {'message': 'api v2: Hello World!'}

@blueprint_v2.route('/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'api v2: This endpoint should return a list of entities ',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'api v2: This endpoint should create an entity',
            'method': request.method,
            'body': request.json
        }

@blueprint_v2.route('/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'api v2: This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'api v2: This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
            'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'api v2: This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }
