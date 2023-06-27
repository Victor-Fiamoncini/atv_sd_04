"""Main program module"""

from flask import Flask, Response, jsonify
from flask_cors import CORS
from rpyc import GenericException

from env import Env
from parse_posts_input_to_list_service import ParsePostsInputToListService
from rpc_connection import RpcConnection


business_app = Flask(__name__)
CORS(business_app)


@business_app.get("/health")
def health_check() -> Response:
    """Server health check function"""

    return jsonify("Business server is alive"), 200


@business_app.post("/posts")
def create_posts() -> Response:
    """Handle /posts HTTP and call with RMI the "save_posts_to_database" routine"""

    try:
        parsed_posts_list = ParsePostsInputToListService().parse_posts_to_json()

        rpc_connection = RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT)
        rpc_connection.bind().call_procedure(
            "save_posts_to_database",
            parsed_posts_list,
        )

        return jsonify("Posts successfully created"), 200
    except GenericException as generic_exception:
        return jsonify(f"An RPC error occurred: {generic_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


if __name__ == "__main__":
    starting_log = f"Starting Business HTTP server at {Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}"

    print(starting_log)

    business_app.run(
        host=Env.BUSINESS_HTTP_SERVER_HOST,
        port=Env.BUSINESS_HTTP_SERVER_PORT,
        debug=True,
    )
