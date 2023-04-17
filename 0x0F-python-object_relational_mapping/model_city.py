#!/usr/bin/python3
"""This script contains the class defintion of a City"""
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from model_state import State

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class City(Base):
    """The City class which identifies SQL records"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey(State.id, ondelete='CASCADE'), nullable=False)


Base.metadata.create_all(engine)
