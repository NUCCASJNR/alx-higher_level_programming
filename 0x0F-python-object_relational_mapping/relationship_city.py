#!/usr/bin/python3

"""
Python file similar to model_state.py named model_city.py that
contains the class definition of a City.
"""

from sqlalchemy import create_engine, Integer, Column
from sqlalchemy import String, Sequence, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base
    Links to the MySQL table cities
    Args:
        id: unique integer, cant be null, primary key, auto generated
        name: String, cant be null
        state_id: integer, foreign key
    """

    __tablename__ = 'cities'
    id = Column(Integer, Sequence('city_id_seq'), unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
