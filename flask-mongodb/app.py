#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# the MongoDB service is available via link-name `mongodb`
db = MongoClient(host='mongodb').test


@app.route('/')
def hello():
    db.hits.update({'name': 'localhost'},
                   {'$inc': {'value': 1}},
                   upsert=True)
    hits = db.hits.find_one({'name': 'localhost'}) or {}
    return 'You hit me %s times.' % hits.get('value', 0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
