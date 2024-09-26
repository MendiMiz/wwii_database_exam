from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base

class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry  = Column(String(200), nullable=False)
    target_priority =Column(Integer)
    city_id = Column(Integer, ForeignKey("cities.city_id"), nullable=False)
    target_type_id = Column(Integer, ForeignKey("target_type.target_type_id"))


    city = relationship("City", back_populates="targets")

    def to_dict(self):
        return {
            "target_id": self.target_id,
            "city_id": self.city_id,
            "target_type_id": self.target_type_id,
            "target_priority": self.target_priority
        }

    def __repr__(self):
        return (f"target_id={self.target_id}, "
                f"city_id ={self.city_id }, " 
                f"target_type_id ={self.target_type_id}, "
                f"target_priority ={self.target_priority}")