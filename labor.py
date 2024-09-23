from sqlalchemy import Column, Integer, String, Float
from project import Base


class Labor(Base):
    __tablename__ = 'labor'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hourly_rate = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Labor(id={self.id}, name={self.name}, hourly_rate={self.hourly_rate})>"
