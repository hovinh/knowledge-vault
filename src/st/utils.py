import streamlit as st
from typing import Any, Dict, List, Tuple
import os
from dataclasses import dataclass
from logzero import logger

MARKDOWN_FOLDER = os.path.join("content", "topics")
MAX_NUMB_TOPICS_PER_ROW = 5
MAX_CHARACTER_IN_TOPIC_NAME = 15


@dataclass
class TopicPage:
    name: str
    title: str
    icon: str
    content: str
    url: str

    @classmethod
    def parse_from_markdown_file_path(cls, file_path: str):
        url = file_path
        name = os.path.splitext(os.path.basename(file_path))[0]
        title, icon = name[0], name[1:]
        content = load_markdown_file_content(file_path)
        return cls(name, title, icon, content, url)

    def get_title(self) -> str:
        return self.title

    def get_icon(self) -> str:
        return self.icon

    def __str__(self):
        output_str = (
            f"name: {self.name}" + f"url: {self.url}" + f"content: {self.content[:10]}"
        )
        return output_str

    def __hash__(self):
        return hash(self.page_name)

    def __eq__(self, other):
        if isinstance(other, TopicPage):
            return self.page_name == other.page_name
        return NotImplemented


class TopicPageManager:
    def __init__(self):
        self.name_page_mapping = dict()

    def add_page(self, page: TopicPage) -> None:
        self.name_page_mapping[page.name] = page

    def get_page_by_name(self, page_name):
        return self.name_page_mapping.get(page_name, None)

    def get_page_list(self):
        return list(self.name_page_mapping.keys())


def get_TopicPageManager() -> Tuple[Dict, List]:

    topic_page_manager = TopicPageManager()
    markdown_file_path_list = get_file_paths_from_folder(MARKDOWN_FOLDER)
    logger.info(f"Scanned markdown files: {markdown_file_path_list}")
    for file_path in markdown_file_path_list:
        topic_page = TopicPage.parse_from_markdown_file_path(file_path)
        logger.info(f"Page loaded: {topic_page}")
        topic_page_manager.add_page(topic_page)

    return topic_page_manager


def set_variable_in_session_state(variable: str, value: Any):
    st.session_state[variable] = value


def get_variable_in_session_state(variable: str):
    return st.session_state.get(variable, None)


def update_clicked_button_state(button_key: str):
    prev_clicked_button = get_variable_in_session_state("cur_clicked_button")
    set_variable_in_session_state("prev_clicked_button", prev_clicked_button)
    set_variable_in_session_state("cur_clicked_button", button_key)


def display_topic_buttons(pages: List):

    page_isClicked_mapping = dict()
    for page_index, page in enumerate(pages):
        is_new_row = page_index % MAX_NUMB_TOPICS_PER_ROW == 0
        col_index = page_index % MAX_NUMB_TOPICS_PER_ROW
        if is_new_row:
            cols = st.columns(MAX_NUMB_TOPICS_PER_ROW)
        with cols[col_index]:
            button_label = f"{page[:MAX_CHARACTER_IN_TOPIC_NAME]}"
            button = st.button(
                button_label,
                key=button_label,
                use_container_width=True,
                on_click=update_clicked_button_state,
                args=[button_label],
            )
            page_isClicked_mapping[page] = button

    return page_isClicked_mapping


def load_topic_page_content(page_name: str) -> None:
    if "page_name_to_topic_page_map" in st.session_state:
        page_name_to_topic_page_map = st.session_state.page_name_to_topic_page_map
        topic_page = page_name_to_topic_page_map[page_name]

        st.set_page_config(
            page_title=topic_page.get_page_title(), page_icon=topic_page.get_icon()
        )
        st.title(topic_page.page_name)
        st.markdown(topic_page.page_content)


def load_markdown_file_content(file_path: str) -> str:
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


def get_file_paths_from_folder(folder_path: str):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)]


def write_line_break(numb_lines: int = 1):
    st.write("<br>" * numb_lines, unsafe_allow_html=True)
