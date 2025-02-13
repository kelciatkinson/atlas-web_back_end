#!/usr/bin/env python3
"""Module for list all function
"""

def list_all(mongo_collection):
    """Lists all documents in a collection.
    """
    if mongo_collection:
        return list(mongo_collection.find())
    return []
