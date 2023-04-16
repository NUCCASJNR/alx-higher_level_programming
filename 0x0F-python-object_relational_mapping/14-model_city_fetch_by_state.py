#!/usr/bin/python3

"""
a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":

    """Establish the database connection to create the engine
    """

    url = ('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    engine = create_engine(url)

    """
    Create the session
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Write query to be executed below
    """

    cities = session.query(City, State).join(City).order_by(City.id)
    for city, state in cities.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
