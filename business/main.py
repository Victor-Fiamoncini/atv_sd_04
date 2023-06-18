"""Main program module"""

from flask import Flask, request

from env import Env
from rpc_connection import RpcConnection


business_app = Flask(__name__)


@business_app.post("/posts")
def create_posts() -> None:
    """Handle /posts HTTP and call with RMI the "convert_posts_to_json" routine"""

    posts = request.data

    RpcConnection(Env.RPC_SERVER_HOST, Env.RPC_SERVER_PORT).bind().call_procedure(
        "convert_posts_to_json",
        posts,
    )


if __name__ == "__main__":
    business_app.run(host=Env.HTTP_SERVER_HOST, port=Env.HTTP_SERVER_PORT, debug=True)
