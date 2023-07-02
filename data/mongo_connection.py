"""This module defines the MongoConnection class"""

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

    def delete_one(self, collection: str, identifier: str) -> None:
        self._client[self.database_name][collection].find_one_and_delete(
            filter={"_id": identifier},
        )

    def update_one(self, collection: str, identifier: str, data: dict) -> None:
        self._client[self.database_name][collection].find_one_and_update(
            filter={"_id": identifier},
            update=data,
        )
