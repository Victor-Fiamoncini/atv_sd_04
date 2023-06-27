"""This module defines the ParsePostsInputToListService class"""

import json

from typing import List

from env import Env


class ParsePostsInputToListService:
    def parse_posts_to_list(self) -> List[dict]:
        with open(Env.POSTS_INPUT_FILEPATH, encoding="utf-8") as posts_file:
            posts_file_text_content = posts_file.read()
            parsed_posts_list = json.loads(posts_file_text_content)

            return parsed_posts_list
