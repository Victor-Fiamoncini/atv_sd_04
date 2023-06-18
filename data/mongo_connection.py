"""This module defines the MongoConnection class"""

from pymongo import MongoClient

from env import Env


class MongoConnection:
    _client: MongoClient = None

    def __init__(self) -> None:
        self._client = MongoClient(
            f"mongodb://{Env.MONGO_HOST}:{Env.MONGO_PORT}/{Env.MONGO_DATABASE_NAME}"
        )

    def insert_many(self, collection: str, data: list) -> None:
        self._client[Env.MONGO_DATABASE_NAME][collection].insert_many(data)
