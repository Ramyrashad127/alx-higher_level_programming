#!/usr/bin/python3
""" import modules """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == '__main__':
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    session = sessionmaker(engine)
    se = session()
    for ob1, ob2 in se.query(City,State).filter(
            City.state_id == State.id).order_by(City.id):
        print(f"{ob2.name}: ({ob1.id}) {ob1.name}")
