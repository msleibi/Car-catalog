#!/usr/bin/env python


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Categories, Base, Items
 
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

category1 = Categories(name = "Soccer")

session.add(category1)
session.commit()

Item1 = Items(name = "Soccer ball", description = "The Standard Soccer ball", category = category1)

session.add(Item1)
session.commit()

Item2 = Items(name = "Soccer shoe", description = "The Standard Soccer shoe", category = category1)

session.add(Item2)
session.commit()


#Items for Basketball

category2 = Categories(name = "Basketball")

session.add(category1)
session.commit()

Item1 = Items(name = "Basketball ball", description = "The Standard Basketball ball", category = category2)

session.add(Item1)
session.commit()

Item2 = Items(name = "Basketball shoe", description = "The Standard Basketball shoe", category = category2)

session.add(Item2)
session.commit()

#Items for Baseball

category3 = Categories(name = "Baseball")

session.add(category3)
session.commit()

Item1 = Items(name = "Baseball ball", description = "The Standard baseball ball", category = category3)

session.add(Item1)
session.commit()


Item2 = Items(name = "Baseball glove", description ="The Standard baseball glove", category = category3)

session.add(Item2)
session.commit()

Item3 = Items(name = "Baseball Bat", description ="The Standard baseball bat", category = category3)

session.add(Item3)
session.commit()


#Items for Frisbee
category4 = Categories(name = "Frisbee")

session.add(category4)
session.commit()


Item1 = Items(name = "Frisbee", description = "The Standard frisbee",category = category4)

session.add(Item1)
session.commit()


#Items for Snowboarding
category5 = Categories(name = "Snowboarding")

session.add(category5)
session.commit()


Item1 = Items(name = "Snowboard", description = "The Standard Snowboard",category = category5)

session.add(Item1)
session.commit()

Item2 = Items(name = "Googgles", description = "The Standard Googgles",category = category5)

session.add(Item2)
session.commit()


#Items for Rock Climbing

category6 = Categories(name = "Rock Climbing")

session.add(category6)
session.commit()


Item1 = Items(name = "Climbing shoe", description = "The Standard Climbing shoe",category = category6)

session.add(Item1)
session.commit()

Item2 = Items(name = "Climbing Hammer", description = "The Standard Climbing Hammer",category = category6)

session.add(Item2)
session.commit()


#Items for Foosball

category7 = Categories(name = "Foosball")

session.add(category7)
session.commit()


Item1 = Items(name = "Foosball", description = "The Standard Foosball",category = category7)

session.add(Item1)
session.commit()


#Items for Skating

category8 = Categories(name = "Skating")

session.add(category8)
session.commit()

Item1 = Items(name = "Roller Skating", description = "The Standard Roller",category = category8)

session.add(Item1)
session.commit()


#Items for Hockey

category9 = Categories(name = "Hockey")

session.add(category9)
session.commit()

Item1 = Items(name = "Hockey stick", description = "The Standard Hockey stick",category = category9)

session.add(Item1)
session.commit()

Item2 = Items(name = "Hockey ball", description = "The Standard Hockey ball",category = category9)

session.add(Item2)
session.commit()


print "added items!"
