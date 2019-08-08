#!/usr/bin/env python


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Categories, Base, Properties
 
engine = create_engine('sqlite:///carcatalogapp.db')


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Properties for Lamborghini

category1 = Categories(name = "Lamborghini")

session.add(category1)
session.commit()

property1 = Properties(model = "Aventador", description = "mid-engine sports car produced by the Italian automotive manufacturer Lamborghini",speed = "349",carEngine = "V12",manufacture = "Lamborghini",carClass ="Sports car(S)",photo = "", category = category1)

session.add(property1)
session.commit()



print "added Car properties!"
