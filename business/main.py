"""Main program module"""

from flask import Flask, Response, jsonify, request
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


@business_app.get("/posts")
def get_posts() -> Response:
    """Handle /posts HTTP and call with RMI the "get_posts_from_database" routine"""

    try:
        rpc_connection = RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT)
        database_posts = rpc_connection.bind().call_procedure(
            "get_posts_from_database", None
        )

        parsed_posts = [
            {
                "document_id": str(post.get("_id", "")),
                "userId": post.get("userId", None),
                "id": post.get("id", None),
                "title": post.get("title", None),
                "body": post.get("body", None),
            }
            for post in database_posts
        ]

        return jsonify(parsed_posts), 200
    except GenericException as generic_exception:
        return jsonify(f"An RPC error occurred: {generic_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


@business_app.post("/posts")
def create_posts() -> Response:
    """Handle /posts HTTP and call with RMI the "save_posts_to_database" routine"""

    try:
        parsed_posts_list = ParsePostsInputToListService().parse_posts_to_list()

        rpc_connection = RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT)
        rpc_connection.bind().call_procedure(
            "save_posts_to_database",
            parsed_posts_list,
        )

        return jsonify("Posts successfully created"), 201
    except GenericException as generic_exception:
        return jsonify(f"An RPC error occurred: {generic_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


@business_app.put("/posts/<id>")
def update_post(id: str) -> Response:
    """Handle /posts HTTP and call with RMI the "update_post_from_database" routine"""

    try:
        rpc_connection = RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT)
        rpc_connection.bind().call_procedure(
            "update_post_from_database",
            id,
            request.json,
        )

        return jsonify(f"Post {id} successfully updated"), 200
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
