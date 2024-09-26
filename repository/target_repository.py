from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError
from config.base import session_factory
from model import Target
from returns.maybe import Maybe, Nothing


def insert_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure("Failed to insert target: " + str(e))


def find_target_by_id(t_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Target)
            .filter(Target.target_id == t_id)
            .first()
        )


def update_target(t_id: int, target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(t_id)
            if maybe_target is Nothing:
                return Failure(f"No target found with id {t_id}")

            target_to_update = session.merge(maybe_target.unwrap())
            target_to_update.target_industry = target.target_industry
            target_to_update.target_priority = target.target_priority
            target_to_update.city_id = target.city_id
            target_to_update.target_type_id = target.target_type_id

            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def delete_target(t_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(t_id)
            if maybe_target is Nothing:
                return Failure(f"No target found with id {t_id}")

            target_to_delete = session.merge(maybe_target.unwrap())
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_all_target():
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Target)
            .all()
        )
