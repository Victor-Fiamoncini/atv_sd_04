"""This module defines the MongoConnection class"""

from pymongo import MongoClient

from env import Env


class MongoConnection:
    host: str = None
    database_name: str = None

    _client: MongoClient = None

    def __init__(self, host: str, database_name: str) -> None:
        self.host = host
        self.database_name = database_name

        self._client = MongoClient(f"mongodb://{host}/{database_name}")

    def insert_many(self, collection: str, data: list) -> None:
        self._client[self.database_name][collection].insert_many(data)
