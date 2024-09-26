from flask import Blueprint, request, jsonify
from jinja2.lexer import Failure
from returns.result import Success

from model import Target
from repository.target_repository import find_target_by_id, get_all_target, update_target, insert_target
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
    try:
        data = request.json
        target = Target(
            target_industry=data.get("target_industry"),
            city_id=data.get("city_id"),
            target_type_id=data.get("target_type_id"),
            target_priority=data.get("target_priority")
        )
        inserted = insert_target(target)
        return jsonify(inserted.unwrap().to_dict()), 201
    except Exception as e:
        return jsonify({"error": e}), 400


@target_blueprint.route("/<int:target_id>", methods=['PUT'])
def update_target_route(target_id: int):
      try:
        data = request.json
        target = Target(
            target_industry=data.get("target_industry"),
            city_id=data.get("city_id"),
            target_type_id=data.get("target_type_id"),
            target_priority=data.get("target_priority")
        )
        update_target(target_id, target)
        return jsonify({"updated" : f"{find_target_by_id(target_id)}"}), 200
      except Exception as e:
            return jsonify({"error": e}), 400


