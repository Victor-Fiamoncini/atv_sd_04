"""This module defines the SavePostsThreadExecutor class"""

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from typing import Generator, List

from mongo_connection import MongoConnection


class SavePostsThreadExecutor:
    mongo_connection: MongoConnection = None
    posts: List[dict] = []

    MAX_THREADS: int = 4

    def __init__(self, mongo_connection: MongoConnection, posts: List[dict]) -> None:
        self.mongo_connection = mongo_connection
        self.posts = posts

    def execute_concurrently(self) -> Generator:
        """Executes the following tasks concurrently"""

        with ThreadPoolExecutor(max_workers=self.MAX_THREADS) as executor:
            save_post_futures = [
                executor.submit(self.mongo_connection.insert_one, "posts", post)
                for post in self.posts
            ]

            for future in futures.as_completed(save_post_futures):
                exception = future.exception()

                yield exception if exception else future.result()
