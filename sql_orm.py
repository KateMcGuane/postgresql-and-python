from sqlalchemy import (
    create_engine, Column , Float ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions form the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# instead of connection to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to tour engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined abouve
session = Session()


# creating the database using declarative base subclass
base.metadata.create_all(db)