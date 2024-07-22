from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    ssn = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    age = Column(Integer)

class Thing(Base):
    __tablename__ = 'thing'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(Integer, ForeignKey('person.ssn'))
    person = relationship("Person")
