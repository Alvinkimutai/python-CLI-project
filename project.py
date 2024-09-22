from sqlalchemy import create_engine, Column, Integer, String, Float, Date 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
import datetime

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)

    def __str__(self) -> str:
        return f'Project Name: {self.name}, Start Date: {self.start_date}, End Date: {self.end_date}, Budget: {self.budget}'
    

DATABASE_URL = 'sqlite:///projects.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


   