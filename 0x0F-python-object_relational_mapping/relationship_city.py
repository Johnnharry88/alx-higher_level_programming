#!/usr/bin/python3
"""Defines a City model and links to the databse"""

from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base, State

class City(Base):
    """Defines City in MySQl database"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
