#!/usr/bin/python3

"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == "__main__":
    """
    Create the engine
    """
    url = ('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    engine = create_engine(url)
    Base.metadata.create_all(engine)

    """
    Create a session
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(City).order_by(City.id).all()
    for state in query:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
