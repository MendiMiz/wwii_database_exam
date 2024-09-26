from flask import Blueprint, request, jsonify

from repository.target_repository import find_target_by_id, get_all_target

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
    

