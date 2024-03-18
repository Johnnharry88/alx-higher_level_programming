#!/usr/bin/python3
"""Defined and state model and inherits from
#SQLAlchemy linking to the MYSQL table states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines a staes from MySql database.
    __tablename__: the name of the MySQL table to store states
    id: The state's id
    name: the state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
