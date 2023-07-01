"""Main program module"""

from rpyc.utils.server import ThreadedServer

from env import Env
from mongo_connection import MongoConnection
from rpc_mongo_database_service import RpcMongoDatabaseService


def main() -> None:
    mongo_connection_01 = MongoConnection(
        host=Env.MONGO_HOST_01,
        database_name=Env.MONGO_DATABASE_NAME_01,
    )
    mongo_connection_02 = MongoConnection(
        host=Env.MONGO_HOST_02,
        database_name=Env.MONGO_DATABASE_NAME_02,
    )
    mongo_connection_03 = MongoConnection(
        host=Env.MONGO_HOST_03,
        database_name=Env.MONGO_DATABASE_NAME_03,
    )

    rpc_mongo_database_service = RpcMongoDatabaseService(
        mongo_connections=[
            mongo_connection_01,
            mongo_connection_02,
            mongo_connection_03,
        ]
    )

    server = ThreadedServer(
        rpc_mongo_database_service,
        hostname=Env.RPC_SERVER_HOST,
        port=Env.RPC_SERVER_PORT,
        protocol_config={"allow_public_attrs": True, "sync_request_timeout": 10},
    )
    server.start()


if __name__ == "__main__":
    print(f"Starting RPC server at {Env.RPC_SERVER_HOST}:{Env.RPC_SERVER_PORT}")

    main()
