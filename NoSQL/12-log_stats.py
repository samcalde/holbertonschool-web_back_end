#!/usr/bin/env python3

"""
Provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log_amount = collection.count_documents()
    print(f"{log_amount} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        current_method_amount = collection.count_documents({'method': method})
        print(f"\tmethod {method}= {current_method_amount}")
    last_line = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{last_line} status check")
