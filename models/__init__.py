#!/usr/bin/python3
"""
This Module is used to create a unique instance of FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
