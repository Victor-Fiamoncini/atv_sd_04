"""This module defines the RpcMongoSavePostsToDatabaseService class"""

from typing import List

import rpyc

from mongo_connection import MongoConnection
from save_posts_to_database_service import SavePostsToDatabaseService


@rpyc.service
class RpcMongoSavePostsToDatabaseService(SavePostsToDatabaseService, rpyc.Service):
    mongo_connections: List[MongoConnection] = []

    def __init__(self, mongo_connections: List[MongoConnection]) -> None:
        super().__init__()

        self.mongo_connections = mongo_connections

    @rpyc.exposed
    def save_posts_to_database(self, *args) -> None:
        posts = args[0][0]

        for mongo_connection in self.mongo_connections:
            mongo_connection.insert_many("posts", posts)
