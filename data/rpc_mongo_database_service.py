"""This module defines the RpcMongoDatabaseService class"""

from random import choice
from typing import List

import rpyc

from database_service import DatabaseService
from mongo_connection import MongoConnection
from save_posts_thread_executor import SavePostsThreadExecutor


@rpyc.service
class RpcMongoDatabaseService(rpyc.Service, DatabaseService):
    mongo_connections: List[MongoConnection] = []

    def __init__(self, mongo_connections: List[MongoConnection]) -> None:
        super().__init__()

        self.mongo_connections = mongo_connections

    @rpyc.exposed
    def get_posts_from_database(self, *args) -> List[dict]:
        mongo_connection = choice(self.mongo_connections)

        return mongo_connection.find_all("posts")

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

    @rpyc.exposed
    def update_post_from_database(self, *args) -> None:
        post_id = args[0][0]
        post_data = args[0][1]

        for mongo_connection in self.mongo_connections:
            mongo_connection.update_one("posts", post_id, post_data)

    @rpyc.exposed
    def delete_post_from_database(self, *args) -> None:
        post_id = args[0][0]

        for mongo_connection in self.mongo_connections:
            mongo_connection.delete_one("posts", post_id)
