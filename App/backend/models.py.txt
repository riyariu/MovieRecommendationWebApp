from sqlalchemy import Column, Integer, String
from .database import Base

class MoviePreference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    preference = Column(String, index=True)
    recommendations = Column(String)
