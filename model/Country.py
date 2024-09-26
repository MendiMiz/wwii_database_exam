

from sqlalchemy import Column, Integer, String, ForeignKey, false
from sqlalchemy.orm import relationship
from config.base import Base

class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), unique=True, nullable=False)

    cities = relationship("City", back_populates="country")


    def to_dict(self):
        return {
            "country_id": self.country_id,
            "country_name": self.country_name
        }

    def __repr__(self):
        return (f"country_id={self.country_id}, "
                f"country_name={self.country_name}")