#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column


class User(BaseModel, Base):
    """Class attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    __tablename__ = "users"
    email = Column(String(128), nullable=false)
    password = Column(String(128), nullable=false)
    first_name = Column(String(128), nullable=false)
    last_name = Column(String(128), nullable=false)
