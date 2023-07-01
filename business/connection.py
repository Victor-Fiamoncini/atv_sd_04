"""This module defines the Connection abstract class"""

from typing import Any

from unimplemented_method_exception import UnimplementedMethodException


class Connection:
    host: str
    port: int

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def bind(self) -> Any:
        """This method binds the connection to a port and host"""

        raise UnimplementedMethodException()

    def call_procedure(self, procedure_name: str, *args) -> Any:
        """This method calls a remote procedure"""

        raise UnimplementedMethodException()
