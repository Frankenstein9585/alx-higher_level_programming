#!/usr/bin/python3
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State)

for state in states:
    print('{}: {}'.format(state.id, state.name))
