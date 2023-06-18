"""Main program module"""

from rpyc.utils.server import ThreadedServer

from env import Env
from mongo_connection import MongoConnection
from rpc_mongo_save_posts_to_database_service import RpcMongoSavePostsToDatabaseService


def main() -> None:
    print(f"Starting RPC server at {Env.RPC_SERVER_HOST}:{Env.RPC_SERVER_PORT}")

    mongo_connection = MongoConnection()
    rpc_mongo_save_posts_to_database_service = RpcMongoSavePostsToDatabaseService(
        mongo_connection
    )

    server = ThreadedServer(
        rpc_mongo_save_posts_to_database_service,
        hostname=Env.RPC_SERVER_HOST,
        port=Env.RPC_SERVER_PORT,
    )
    server.start()


if __name__ == "__main__":
    main()
