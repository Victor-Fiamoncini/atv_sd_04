"""This module defines the class DatabaseService abstract class"""

from unimplemented_method_exception import UnimplementedMethodException


class DatabaseService:
    def get_posts_from_database(self, *args) -> None:
        """Executes the fetch of data from provided database"""

        raise UnimplementedMethodException()

    def save_posts_to_database(self, *args) -> None:
        """Executes the creation of posts data to provided database"""

        raise UnimplementedMethodException()
