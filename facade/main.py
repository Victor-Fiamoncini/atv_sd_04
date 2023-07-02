"""Main program module"""

import json

import requests

from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from requests.exceptions import HTTPError, RequestException

from env import Env


facade_app = Flask(__name__)
CORS(facade_app)


@facade_app.get("/health")
def health_check() -> Response:
    """Server health check function"""

    return jsonify("Facade server is alive"), 200


@facade_app.get("/posts")
def get_posts() -> Response:
    """Handle GET /posts HTTP to business server"""

    try:
        response = requests.get(
            url=f"{Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}/posts",
            timeout=120,
        )

        return jsonify(response.json()), 200
    except HTTPError as http_error:
        return jsonify(f"An HTTP error occurred: {http_error}"), 400
    except RequestException as request_exception:
        return jsonify(f"An HTTP request error occurred: {request_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


@facade_app.post("/posts")
def create_posts() -> Response:
    """Handle POST /posts HTTP to business server"""

    try:
        requests.post(
            url=f"{Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}/posts",
            timeout=120,
        )

        return jsonify("Posts successfully created"), 201
    except HTTPError as http_error:
        return jsonify(f"An HTTP error occurred: {http_error}"), 400
    except RequestException as request_exception:
        return jsonify(f"An HTTP request error occurred: {request_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


@facade_app.put("/posts/<id>")
def update_post(id: str) -> Response:
    """Handle PUT /posts HTTP to business server"""

    try:
        requests.put(
            url=f"{Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}/posts/{id}",
            timeout=120,
            data=json.dumps(request.json),
            headers={"Content-Type": "application/json"},
        )

        return jsonify(f"Post {id} successfully updated"), 200
    except HTTPError as http_error:
        return jsonify(f"An HTTP error occurred: {http_error}"), 400
    except RequestException as request_exception:
        return jsonify(f"An HTTP request error occurred: {request_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


@facade_app.delete("/posts/<id>")
def delete_post(id: str) -> Response:
    """Handle DELETE /posts HTTP to business server"""

    try:
        requests.delete(
            url=f"{Env.BUSINESS_HTTP_SERVER_HOST}:{Env.BUSINESS_HTTP_SERVER_PORT}/posts/{id}",
            timeout=120,
        )

        return jsonify(f"Post {id} successfully deleted"), 200
    except HTTPError as http_error:
        return jsonify(f"An HTTP error occurred: {http_error}"), 400
    except RequestException as request_exception:
        return jsonify(f"An HTTP request error occurred: {request_exception}"), 400
    except Exception as exception:
        return jsonify(f"Internal server error: {exception}"), 500


if __name__ == "__main__":
    starting_log = f"Starting Facade HTTP server at {Env.FACADE_HTTP_SERVER_HOST}:{Env.FACADE_HTTP_SERVER_PORT}"

    print(starting_log)

    facade_app.run(
        host=Env.FACADE_HTTP_SERVER_HOST,
        port=Env.FACADE_HTTP_SERVER_PORT,
        debug=True,
    )
