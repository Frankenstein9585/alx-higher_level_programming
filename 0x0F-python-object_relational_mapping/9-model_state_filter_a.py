#!/usr/bin/python3
"""This script lists all the state objects from a given db"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        if 'a' in state.name:
            print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    main()
