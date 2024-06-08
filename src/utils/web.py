import streamlit as st
from typing import Any, Dict, List, Tuple
import os
from logzero import logger

from src.topic_page import TopicPage, TopicPageManager
from src.utils.data import get_file_paths_from_folder, load_markdown_file_content

MARKDOWN_FOLDER = os.path.join("content", "topics")
MAX_NUMB_TOPICS_PER_ROW = 5
MAX_CHARACTER_IN_TOPIC_NAME = 15


def get_TopicPageManager() -> Tuple[Dict, List]:
    """
    Retrieves a TopicPageManager instance by scanning the markdown files in the specified folder.

    Returns:
        Tuple[Dict, List]: A tuple containing a dictionary and a list. The dictionary is an empty dictionary, and the list contains the TopicPage objects parsed from the markdown files.
    """
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
    """
    Updates the state of the clicked button in the session state.

    Args:
        button_key (str): The key of the button that was clicked.

    Returns:
        None
    """
    logger.info(f"Updated button state: {button_key}")
    prev_clicked_button = get_variable_in_session_state("cur_clicked_button")
    set_variable_in_session_state("prev_clicked_button", prev_clicked_button)
    set_variable_in_session_state("cur_clicked_button", button_key)


def is_first_web_load():
    """
    Checks if it is the first time the web page is being loaded.

    Returns:
        bool: True if it is the first time the web page is being loaded, False otherwise.
    """
    first_load = get_variable_in_session_state("is_first_web_load")
    if first_load is None:
        set_variable_in_session_state("is_first_web_load", False)
        return True
    return False


def display_topic_buttons(pages: List):
    """
    Displays a set of buttons for each page in the given list of pages.
    When a button is clicked, the update_clicked_button_state function is called with
    the page name as an argument.

    Args:
        pages (List): A list of strings representing the names of the pages.

    Returns:
        dict: A dictionary mapping each page name to its corresponding button object.

    """
    page_isClicked_mapping = dict()
    for page_index, page in enumerate(pages):
        is_new_row = page_index % MAX_NUMB_TOPICS_PER_ROW == 0
        col_index = page_index % MAX_NUMB_TOPICS_PER_ROW
        if is_new_row:
            cols = st.columns(MAX_NUMB_TOPICS_PER_ROW)
        with cols[col_index]:
            button_label = f"**{page[:MAX_CHARACTER_IN_TOPIC_NAME]}**"
            button = st.button(
                button_label,
                key=button_label,
                use_container_width=True,
                on_click=update_clicked_button_state,
                args=[page],
            )
            page_isClicked_mapping[page] = button

    return page_isClicked_mapping


def write_line_break(numb_lines: int = 1):
    st.write("<br>" * numb_lines, unsafe_allow_html=True)


def write_horizontal_line():
    st.markdown("---")


def write_markdown_content(md_file_path: str):
    content = load_markdown_file_content(md_file_path)
    st.markdown(content, unsafe_allow_html=True)
