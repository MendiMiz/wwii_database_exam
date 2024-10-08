from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base

class TargetType(Base):
    __tablename__ = "target_types"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(200), unique=True, nullable=False)

    targets = relationship("Target", back_populates="target_type")

    def to_dict(self):
        return {
            "target_type_id": self.target_type_id,
            "target_type_name": self.target_type_name
        }

    def __repr__(self):
        return (f"target_type_id={self.target_type_id}, "
                f"target_type_name={self.target_type_name}")