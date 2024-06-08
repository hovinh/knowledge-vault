import streamlit as st
from src.st.utils import (
    get_TopicPageManager,
    display_topic_buttons,
    write_line_break,
    load_markdown_file_content,
    get_variable_in_session_state,
    update_clicked_button_state,
)
from logzero import logger
import os

### SET PAGE CONFIG AND LOAD RELEVANT CONFIG FILES
st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="🧠",
    layout="centered",
    menu_items={
        "About": "# this is a header. This is a cool app!",
    },
)
topic_page_manager = get_TopicPageManager()
all_pages = topic_page_manager.get_page_list()
displayed_pages = st.session_state.get("displayed_pages", all_pages)

intro_markdown_file_path = os.path.join("content", "intro.md")

logger.info(f"All pages: {all_pages}")
logger.info(f"Displayed pages: {displayed_pages}")

### PAGE CONTENT
st.title("Knowledge Vault")
st.markdown(load_markdown_file_content(intro_markdown_file_path))

search_text = st.text_input("Enter your search query:", key="search-bar")
if search_text != "":
    st.markdown("Feature is not available yet.")
write_line_break()

st.markdown("Topics")
page_isClicked_mapping = display_topic_buttons(displayed_pages)
prev_clicked_button = get_variable_in_session_state("prev_clicked_button")
cur_clicked_button = get_variable_in_session_state("cur_clicked_button")
logger.info(f"prev_clicked_button: {prev_clicked_button}")
logger.info(f"cur_clicked_button: {cur_clicked_button}")

if cur_clicked_button is not None:
    is_clicked_twice = cur_clicked_button == prev_clicked_button
    if not is_clicked_twice:
        page = topic_page_manager.get_page_by_name(cur_clicked_button)
        st.markdown("---")
        st.markdown(page.content)
    else:
        update_clicked_button_state(None)
