from sqlalchemy import Column, Integer
from base import Base

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    winner_id = Column(Integer)
