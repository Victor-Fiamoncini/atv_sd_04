"""This module defines the RpcConnection class"""

import rpyc

from rpyc import Connection as RpycConnection

from connection import Connection


class RpcConnection(Connection):
    rpyc_connection: RpycConnection = None

    def __init__(self, host: str, port: int) -> None:
        Connection.__init__(self, host, port)

    def bind(self) -> Connection:
        self.rpyc_connection = rpyc.connect(self.host, self.port)

        return self

    def call_procedure(self, procedure_name: str, *args) -> None:
        if not self.rpyc_connection or not procedure_name:
            return

        procedure = getattr(self.rpyc_connection.root, procedure_name)
        procedure(args)
