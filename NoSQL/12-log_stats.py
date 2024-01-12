#!/usr/bin/env python3

"""
Using Mongo through python
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic:
    """
    mongo_collection.find({'topic': topic})
