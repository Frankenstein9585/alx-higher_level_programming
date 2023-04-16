#!/usr/bin/python3
"""This script contains the class defintion of a State"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
#                        format(sys.argv[1], sys.argv[2], sys.argv[3]),
#                        pool_pre_ping=True, echo=True)
#
# Session = sessionmaker(bind=engine)
# session = Session()

Base = declarative_base()


class State(Base):
    """The state class which identifies SQL records"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
