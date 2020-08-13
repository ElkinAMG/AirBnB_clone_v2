#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

t_storage = getenv('HBNB_TYPE_STORAGE')

"""Conditional to check the storage type (file or database)"""
if t_storage == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
