import streamlit as st
from typing import Dict, List, Tuple
import yaml
import os
from dataclasses import dataclass

PAGES_FOLDER = "pages"
MARKDOWN_FOLDER = os.path.join("data", "topics")
MAX_NUMB_TOPICS_PER_ROW = 5


@dataclass
class TopicPage:
    url: str
    page_name: str
    page_content: str

    def get_page_title(self) -> str:
        return self.page_name.split(" ")[1]

    def get_icon(self) -> str:
        return self.page_name.split(" ")[0]

    def __str__(self):
        return f"url: {self.url} | page_name: {self.page_name} | page_content: {self.page_content[:20]}"

    def __hash__(self):
        return hash(self.page_name)

    def __eq__(self, other):
        if isinstance(other, TopicPage):
            return self.page_name == other.page_name
        return NotImplemented


def generate_topic_pages_info_list_from_pages_folder() -> Tuple[Dict, List]:

    def parse_python_file_name_to_TopicPage(python_file_name: str) -> TopicPage:
        url = os.path.join(PAGES_FOLDER, python_file_name)
        page_name = os.path.splitext(python_file_name)[0].replace("_", " ")
        markdown_file_name = python_file_name.replace("py", "md")
        markdown_file_path = os.path.join(MARKDOWN_FOLDER, markdown_file_name)
        page_content = load_page_content_from_markdown(markdown_file_path)
        return TopicPage(url, page_name, page_content)

    page_name_to_topic_page_map = dict()
    topic_page_list = list()
    python_file_name_list = [path for path in os.listdir(PAGES_FOLDER) if ".py" in path]
    for python_file_name in python_file_name_list:
        topic_page = parse_python_file_name_to_TopicPage(python_file_name)
        page_name_to_topic_page_map[topic_page.page_name] = topic_page
        topic_page_list.append(topic_page)

    return page_name_to_topic_page_map, topic_page_list


def display_topic_shortcuts(topic_page_list: List):
    topic_page_is_clicked_dict = dict()
    for page_index, topic_page in enumerate(topic_page_list):
        is_new_row = page_index % MAX_NUMB_TOPICS_PER_ROW == 0
        col_index = page_index % MAX_NUMB_TOPICS_PER_ROW
        if is_new_row:
            cols = st.columns(MAX_NUMB_TOPICS_PER_ROW)
        with cols[col_index]:
            button = st.button(topic_page.page_name)
            topic_page_is_clicked_dict[topic_page] = button

    return topic_page_is_clicked_dict


def load_topic_page_content(page_name: str) -> None:
    if "page_name_to_topic_page_map" in st.session_state:
        page_name_to_topic_page_map = st.session_state.page_name_to_topic_page_map
        topic_page = page_name_to_topic_page_map[page_name]

        st.set_page_config(
            page_title=topic_page.get_page_title(), page_icon=topic_page.get_icon()
        )
        st.title(topic_page.page_name)
        st.markdown(topic_page.page_content)


def load_page_content_from_markdown(file_path: str) -> str:
    """
    Loads the content of a Markdown file from the given file path.

    Parameters:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The content of the Markdown file as a string.
    """
    with open(file_path, "r") as file:
        content = file.read()
    return content


def load_yaml(yaml_file_path: str) -> Dict:
    with open(yaml_file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


def write_line_break(numb_lines: int = 1):
    st.write("<br>" * numb_lines, unsafe_allow_html=True)
