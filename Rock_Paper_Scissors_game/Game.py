from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    winner_id = Column(Integer)
