from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from project import Base  # Ensure Base is imported

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    progress = Column(Float, default=0.0)

    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, project_id={self.project_id}, progress={self.progress})>"
