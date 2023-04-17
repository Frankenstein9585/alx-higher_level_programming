#!/usr/bin/python3
"""This script prints all city objects from the database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """The main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(City).order_by(City.id)
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == '__main__':
    main()
