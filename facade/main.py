"""Main program module"""

import requests

from flask import Flask, Response, jsonify

from env import Env


facade_app = Flask(__name__)


@facade_app.get("/health")
def health_check() -> Response:
    """Server health check function"""

    return "Facade server is alive", 200


@facade_app.post("/posts")
def create_posts() -> Response:
    """Handle /posts HTTP to business server"""

    try:
        requests.get(
            url=f"{Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}/posts",
            timeout=120,
        )

        return jsonify("Posts successfully created"), 200
    except:
        return jsonify("Server error"), 500


if __name__ == "__main__":
    starting_log = f"Starting Facade HTTP server at {Env.FACADE_HTTP_SERVER_HOST}:{Env.FACADE_HTTP_SERVER_PORT}"

    print(starting_log)

    facade_app.run(
        host=Env.FACADE_HTTP_SERVER_HOST,
        port=Env.FACADE_HTTP_SERVER_PORT,
        debug=True,
    )
