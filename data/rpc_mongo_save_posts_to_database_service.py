"""This module defines the RpcMongoSavePostsToDatabaseService class"""

from typing import List

import rpyc

from mongo_connection import MongoConnection
from save_posts_to_database_service import SavePostsToDatabaseService
from save_posts_thread_executor import SavePostsThreadExecutor


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
            save_posts_thread_executor = SavePostsThreadExecutor(
                mongo_connection=mongo_connection,
                posts=posts,
            )

            for _ in save_posts_thread_executor.execute_concurrently():
                pass
