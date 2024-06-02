#!/usr/bin/python3
"""
initialize the tables package
"""
from os import getenv
from tables.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
