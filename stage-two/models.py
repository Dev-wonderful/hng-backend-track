#!/usr/bin/python3
"""defining the schema for users collection"""
from mongoengine import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host = getenv('MONGO_CONNECTION_URI', '127.0.0.1')
try:
    connect(db='hngbackend', host=host, port=27017)
except Exception as error:
    print(f'{type(error).__name__}: {error}')


class Users(Document):
    """users Collection in KitchenQuest db"""
    name = StringField(max_length=120, required=True, unique=False)
