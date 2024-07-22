import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    password = Column (String(250))

class Characters(Base):
    __tablename__ = 'characters'
   
    charId = Column(Integer, primary_key=True)
    charName = Column(String(250))
    charDescription = Column(String(2500))
    charOrigin = Column(String(250))
    
class Planets(Base):
    __tablename__ = 'planets'

    planetId = Column (Integer, primary_key=True)
    planetName = Column (String(250))
    planetDescription = Column (String (2500))

class Favourites(Base):
    __tablename__ = 'favourites'

    favId = Column(Integer, primary_key=True)
    favUserID = Column (Integer, ForeignKey('user.id'))
    favCharID = Column(Integer, ForeignKey('characters.id'))
    favPlanetID = Column(Integer, ForeignKey('planets.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
