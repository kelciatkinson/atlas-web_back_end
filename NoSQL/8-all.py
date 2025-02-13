#!/usr/bin/env python3

def list_all(mongo_collection):
    """Lists all documents in a collection.
    """
    if mongo_collection:
        return list(mongo_collection.find())
    return []