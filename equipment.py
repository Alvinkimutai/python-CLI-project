from sqlalchemy import Column, Integer, String, Float
from project import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rental_cost_per_day = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Equipment(id={self.id}, name={self.name}, rental_cost_per_day={self.rental_cost_per_day})>"