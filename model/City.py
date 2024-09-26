from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from config.base import Base

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(200), unique=True, nullable=False)
    country_id = Column(String(200), nullable=False)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    country = relationship("Country", back_populates="cities")

    def to_dict(self):
        return {
            "city_id": self.city_id,
            "city_name": self.city_name,
            "country_id": self.country_id,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def __repr__(self):
        return (f"city_id={self.city_id}, "
                f"city_name={self.city_name}, "
                f"country_id={self.country_id}, "
                f"latitude={self.latitude}, "
                f"longitude={self.longitude}")