"""This module defines the RpcConnection class"""

from typing import Any

import rpyc

from rpyc import Connection as RpycConnection

from connection import Connection


class RpcConnection(Connection):
    rpyc_connection: RpycConnection = None

    def __init__(self, host: str, port: int) -> None:
        Connection.__init__(self, host, port)

    def bind(self) -> Connection:
        self.rpyc_connection = rpyc.connect(
            self.host,
            self.port,
            config={"allow_public_attrs": True, "sync_request_timeout": 10},
        )

        return self

    def call_procedure(self, procedure_name: str, *args) -> Any:
        if not self.rpyc_connection or not procedure_name:
            return

        procedure = getattr(self.rpyc_connection.root, procedure_name)
        result = procedure(args)

        return result
