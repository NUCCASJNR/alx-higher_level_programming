#!/usr/bin/python3

"""
This script Improve the files model_city.py and model_state.py
and save them as relationship_city.py and relationship_state.py
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from model_city import City
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

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_city.states = new_state
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
