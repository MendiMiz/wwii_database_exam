from flask import Blueprint, request, jsonify
from jinja2.lexer import Failure
from returns.result import Success

from repository.target_repository import find_target_by_id, get_all_target
from service.target_service import create_target_from_json

target_blueprint = Blueprint("target", __name__)



@target_blueprint.route('/search', methods=['GET'])
def target_by_id():
    target_id = int(request.args.get("id"))
    target = find_target_by_id(target_id).unwrap()
    return jsonify(target.to_dict()), 200

@target_blueprint.route('/get_all', methods=['GET'])
def all_targets():
    return (get_all_target()
            .map(lambda targets: [t.to_dict() for t in targets])
            .map(lambda li: (jsonify(li), 200))
            .value_or((jsonify({}), 400)))

@target_blueprint.route('/create', methods=['POST'])
def create_target():
    target_json = request.json
    result = create_target_from_json(target_json)
    if result is Success:
        return jsonify(result.unwrap().to_dict()), 201
    else:
        return jsonify({"error": result.failure()}), 400


