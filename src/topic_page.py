import os
from typing import List
from dataclasses import dataclass
from logzero import logger
from src.utils.data import load_markdown_file_content
import json


@dataclass
class TopicPage:
    """
    Represents a topic page.

    Attributes:
        name (str): The name of the topic.
        content (str): The content of the topic.
        url (str): The URL of the topic.
    """

    name: str
    gist_urls: List[str]
    content: str
    url: str

    @classmethod
    def parse_from_markdown_file_path(cls, file_path: str):
        url = file_path
        name = os.path.splitext(os.path.basename(file_path))[0]
        content = load_markdown_file_content(file_path)
        gist_urls, content = cls.extract_gist_urls(content)
        return cls(name, gist_urls, content, url)

    @classmethod
    def extract_gist_urls(cls, content: str):
        has_gist_url = True if ("has_gist" in content[:100]) else False
        gist_urls = list()
        if has_gist_url:
            logger.info("Has gist header.")
            splitted_content = content.split("---")
            headers, content = splitted_content[0], "".join(splitted_content[1:])
            logger.info(f"headers: {headers}")
            gist_dict = json.loads(headers)
            logger.info(f"gist dict: {gist_dict}")
            if gist_dict["has_gist"]:
                gist_urls = gist_dict["content"]

        return gist_urls, content

    def __str__(self):
        output_str = (
            f"name: {self.name}"
            + f"\t url: {self.url}"
            + f"\t content: {self.content[:10]}"
        )
        return output_str

    def query_exact_match(self, text: str):
        return text.lower() in self.content.lower()


class TopicPageManager:
    """
    A class that manages a collection of `TopicPage` objects.

    Attributes:
        name_page_mapping (dict): A dictionary mapping page names to `TopicPage` objects.
    """

    def __init__(self):
        self.name_page_mapping = dict()

    def add_page(self, page: TopicPage) -> None:
        self.name_page_mapping[page.name] = page

    def get_page_by_name(self, page_name):
        return self.name_page_mapping.get(page_name, None)

    def get_page_list(self):
        return sorted(list(self.name_page_mapping.keys()))
