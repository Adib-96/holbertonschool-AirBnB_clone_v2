#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """returns the list of City instances
        with state_id equals to the current State.id"""
        from models import storage
        from models.city import City
        _list = []
        res = storage.all(City)
        for v in res.values():
            if v.state_id == self.id:
                _list.append(v)
        return _list
