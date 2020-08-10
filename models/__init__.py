#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

t_storage = getenv('HBNB_TYPE_STORAGE')

if t_storage == 'db':
    pass
else:
    storage = FileStorage()
    storage.reload()
