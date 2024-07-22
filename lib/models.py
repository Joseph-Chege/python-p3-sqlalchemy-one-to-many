from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

#Game model
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    genre = Column(String(), nullable=False)
    platform = Column(String(), nullable=False)
    price = Column(Integer(), nullable=False)

    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(title="{self.title}", genres="{self.genre}", platform="{self.platform}")'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer(), nullable=False)
    comment = Column(String(), nullable=False)
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(score={self.score}, comment="{self.comment}", game_id="{self.game_id}")'

    