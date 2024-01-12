#!/usr/bin/env python3

"""
Using Mongo through python
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic:
    """
    school_list = mongo_collection.find({'topics': topic})
    return school_list
