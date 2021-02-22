import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
    

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Type = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))

class Planets(Base):
    __tablename__ = 'planets'
    planets_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String, nullable=False)
    skin = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    characters_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer,  nullable=False)
    orbital = Column(Integer,  nullable=False)
    period = Column(Integer,  nullable=False)
    rotation_period = Column(Integer,  nullable=False)
    diameter = Column(Integer,  nullable=False)


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')