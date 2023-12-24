#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DbStorage
    storage = DbStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
