#!/usr/bin/python3

"""
a script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
import sys

if __name__ == "__main__":
    """
    Create the engine
    """
    url = ('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    engine = create_engine(url)

    """
    Create a session
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Write the sql query to be executed below
    """

    """
    Add the new state
    """
    new_state = State(name="Louisiana")

    """
    Add the new created object to the session
    """
    session.add(new_state)
    session.commit()
    print(f"{new_state.id}")
    session.close()
