"""This module defines the Env class"""

from os.path import dirname, join


class Env:
    BUSINESS_HTTP_SERVER_HOST = "business"
    BUSINESS_HTTP_SERVER_PORT = 3001

    POSTS_INPUT_FILEPATH = join(dirname(__file__), "input", "posts.json")

    RPC_SERVER_HOST = "data"
    RPC_SERVER_PORT = 3002
