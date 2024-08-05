from sqlalchemy import Column, Integer, String
from base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    wins = Column(Integer, default=0)
    games_played = Column(Integer, default=0)
