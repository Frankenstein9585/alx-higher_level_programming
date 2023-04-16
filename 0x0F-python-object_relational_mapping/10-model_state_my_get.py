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

    states = session.query(State)

    for state in states:
        if sys.argv[4] == state.name:
            print(state.id)
            break
        else:
            print('Not found')
            break


if __name__ == '__main__':
    main()
