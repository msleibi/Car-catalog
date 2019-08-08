import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Categories(Base):
    __tablename__ = 'categories'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Properties(Base):
    __tablename__ = 'properties'


    model =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    speed = Column(String(50))
    carEngine = Column(String(50),nullable = False)
    manufacture = Column(String(50),nullable = False)
    carClass = Column(String(50),nullable = False)
    photo = Column(String(250),nullable = True)
    categories_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship(Categories)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       #Returns object data in easily serializeable format
       return {
           'model'        : self.name,
           'description'  : self.description,
           'id'           : self.id,
           'speed'        : self.speed,
           'carEngine'    : self.carEngine,
           'manufacture'  : self.manufacture,
           'carClass'     : self.carClass,
           }

engine = create_engine('sqlite:///carcatalogapp.db')
 

Base.metadata.create_all(engine)
