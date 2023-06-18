"""This module defines the RpcMongoSavePostsToDatabaseService class"""

import json

import rpyc

from mongo_connection import MongoConnection
from save_posts_to_database_service import SavePostsToDatabaseService


@rpyc.service
class RpcMongoSavePostsToDatabaseService(SavePostsToDatabaseService, rpyc.Service):
    mongo_connection: MongoConnection = None

    def __init__(self, mongo_connection: MongoConnection) -> None:
        super().__init__()

        self.mongo_connection = mongo_connection

    @rpyc.exposed
    def save_posts_to_database(self, *args) -> None:
        posts = json.loads(args[0][0])

        self.mongo_connection.insert_many("posts", posts)
