import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
 
Base = declarative_base()
 
class Categories(Base):
    __tablename__ = 'categories'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Items(Base):
    __tablename__ = 'items'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(Integer,nullable = False)
    manufacture = Column(String(50),nullable = False)
    createdate = Column(DateTime, default=datetime.datetime.utcnow)
    categories_id = Column(Integer,ForeignKey('categories.id'))
    category = relationship(Categories)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       #Returns object data in easily serializeable format
       return {
           'name'         : self.name,
           'description'  : self.description,
           'id'           : self.id,
           'price'        : self.price,
           'manufacture'  : self.manufacture,
           }

engine = create_engine('sqlite:///catalogapp.db')
 

Base.metadata.create_all(engine)
