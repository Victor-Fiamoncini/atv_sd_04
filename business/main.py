"""Main program module"""

from flask import Flask, request, jsonify

from env import Env
from rpc_connection import RpcConnection


business_app = Flask(__name__)


@business_app.post("/posts")
def create_posts() -> None:
    """Handle /posts HTTP and call with RMI the "save_posts_to_database" routine"""

    try:
        posts = request.data

        if not posts:
            return jsonify("Posts not provided"), 400

        RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT).bind().call_procedure(
            "save_posts_to_database",
            posts,
        )

        return jsonify("Posts successfully created"), 200
    except:
        return jsonify("Server error"), 500


if __name__ == "__main__":
    print(f"Starting HTTP server at {Env.HTTP_SERVER_HOST}:{Env.HTTP_SERVER_PORT}")

    business_app.run(host=Env.HTTP_SERVER_HOST, port=Env.HTTP_SERVER_PORT, debug=True)
