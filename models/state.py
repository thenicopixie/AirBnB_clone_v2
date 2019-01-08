#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='states')

    @property
    def cities(self):
        """return the list of City instances with the state_id
        equal to the current State.id
        """
        return [value for value in models.storage.all(City).value()
                if value.state_id == self.id]
