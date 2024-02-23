#!/usr/bin/python3
""" import modules """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    session = sessionmaker(engine)
    se = session()
    data = se.query(State).order_by(State.id).first()
    if data is None:
        print('Nothing')
    else:
            print(f'{data.id}: {data.name}')
