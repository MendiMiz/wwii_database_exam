from returns.result import Result, Failure

from model import Target
from repository.target_repository import insert_target


def create_target_from_json(target_json) -> Result[Target, str]:
    try:
        target = Target(
            city_id=target_json['city_id'],
            target_industry=target_json['target_industry'],
            target_priority=target_json['target_priority'],
            target_type_id=target_json['target_type_id']
        )
        return insert_target(target)

    except KeyError as e:
        return Failure(f"Missing field: {str(e)}")
    except Exception as e:
        return Failure(str(e))