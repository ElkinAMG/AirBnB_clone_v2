#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey


class City(BaseModel, Base):
    """ The city class attributes"""
    state_id = ""
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

