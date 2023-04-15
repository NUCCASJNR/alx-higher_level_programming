#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mydb.sqlite')

Session = sessionmaker(bind=engine)
session = Session()

State = session.query(State).order_by(states.id.asc()).all()
for state in State:
    print(state.id, state.name)
