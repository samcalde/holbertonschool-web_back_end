#!/usr/bin/env python3

"""
Using Mongo through python
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    school = {'name': name}
    add_topic = {'$set': {'topics': topics}}
    mongo_collection.update(school, add_topic)
