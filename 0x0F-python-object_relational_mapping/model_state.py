#!/usr/bin/python3
""" new table """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

tb = declarative_base()


class State(tb):
    """ new table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
