"""This module defines the MongoConnection class"""

from bson import ObjectId
from typing import List

from pymongo import MongoClient


class MongoConnection:
    host: str = None
    database_name: str = None

    _client: MongoClient = None

    def __init__(self, host: str, database_name: str) -> None:
        self.host = host
        self.database_name = database_name

        self._client = MongoClient(f"mongodb://{host}/{database_name}")

    def insert_one(self, collection: str, data: dict) -> None:
        self._client[self.database_name][collection].insert_one(data)

    def find_all(self, collection: str) -> List[dict]:
        documents = self._client[self.database_name][collection].find()

        return [document for document in documents]

    def update_one(self, collection: str, identifier: str, data: dict) -> None:
        self._client[self.database_name][collection].update_one(
            {"_id": ObjectId(identifier)},
            {"$set": data},
        )

    def delete_one(self, collection: str, identifier: str) -> None:
        self._client[self.database_name][collection].delete_one(
            {"_id": ObjectId(identifier)},
        )
