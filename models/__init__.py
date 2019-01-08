#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.state import State

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
