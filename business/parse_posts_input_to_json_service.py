"""This module defines the ParsePostsInputToJsonService class"""

import json

from env import Env


class ParsePostsInputToJsonService:
    def parse_posts_to_json(self) -> str:
        with open(Env.POSTS_INPUT_FILEPATH, encoding="utf-8") as posts_file:
            posts_file_text_content = posts_file.read()
            parsed_posts_json = json.loads(posts_file_text_content)

            return parsed_posts_json
