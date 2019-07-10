from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catigories, Base, Items
 
engine = create_engine('sqlite:///catalogapp.db')
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



#Items for Soccer
category1 = Catigories(name = "Soccer")

session.add(category1)
session.commit()

Item1 = Items(name = "Soccer ball", description = "The Standard soccer ball",category = category1)

session.add(Item1)
session.commit()


Item2 = Items(name = "Soccer shoe", description ="The Standard soccer boot", category = category1)

session.add(Item2)
session.commit()


#Items for Basketball
category2 = Catigories(name = "Basketball")

session.add(category2)
session.commit()

Item1 = Items(name = "Basket ball", description = "The Standard basket ball",category = category2)

session.add(Item1)
session.commit()


Item2 = Items(name = "Basketball boot", description ="The Standard basketball boot", category = category2)

session.add(Item2)
session.commit()



print "added items!"
