from sqlalchemy import Column, Integer, String, Float
from project import Base


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit_cost = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Material(id={self.id}, name={self.name}, unit_cost={self.unit_cost}, quantity={self.quantity})>"
