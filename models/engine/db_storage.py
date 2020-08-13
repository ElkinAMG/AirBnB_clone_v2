#!/usr/bin/python3
"""Contains the DBStorage class"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Our class for database storage"""

    """Private class attributes"""
    __engine = None
    __session = None

    """Public instance methods"""
    def __init__(self):
        """Initializes the instance"""
