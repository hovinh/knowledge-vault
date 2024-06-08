import os
from dataclasses import dataclass

from src.utils.data import load_markdown_file_content


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
    content: str
    url: str

    @classmethod
    def parse_from_markdown_file_path(cls, file_path: str):
        url = file_path
        name = os.path.splitext(os.path.basename(file_path))[0]
        content = load_markdown_file_content(file_path)
        return cls(name, content, url)

    def __str__(self):
        output_str = (
            f"name: {self.name}"
            + f"\t url: {self.url}"
            + f"\t content: {self.content[:10]}"
        )
        return output_str


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
