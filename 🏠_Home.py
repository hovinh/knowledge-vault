import streamlit as st
from logzero import logger
import os

from utils.web import (
    display_topic_buttons,
    get_TopicPageManager,
    is_first_web_load,
    get_variable_in_session_state,
    set_variable_in_session_state,
    update_clicked_button_state,
    write_horizontal_line,
    write_line_break,
    write_markdown_content,
)

### SET PAGE CONFIG AND LOAD RELEVANT CONFIG FILES
st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="🧠",
    layout="centered",
    menu_items={
        "About": "# this is a header. This is a cool app!",
    },
)

if is_first_web_load():  # prevent from file loading overhead
    logger.info("First load: create TopicPageManager instance.")
    topic_page_manager = get_TopicPageManager()
    set_variable_in_session_state("topic_page_manager", topic_page_manager)
else:
    logger.info("NOT first load: load TopicPageManager from session state.")
    topic_page_manager = get_variable_in_session_state("topic_page_manager")

all_pages = topic_page_manager.get_page_list()
displayed_pages = get_variable_in_session_state("displayed_pages")
displayed_pages = displayed_pages if displayed_pages is not None else all_pages
intro_markdown_file_path = os.path.join("content", "intro.md")
icon_markdown_file_path = os.path.join("content", "icons.md")

logger.info(f"All pages: {all_pages}")
logger.info(f"Displayed pages: {displayed_pages}")

### PAGE CONTENT
st.title("Knowledge Vault")
write_markdown_content(intro_markdown_file_path)

search_text = st.text_input("Enter your search query:", key="search-bar")
prev_search_text = get_variable_in_session_state("search_text")
logger.info(f"New search text: {search_text}")
logger.info(f"Prev search text: {prev_search_text}")
if search_text != "":
    logger.info(f"Non-empty search text: {search_text}")
    set_variable_in_session_state("search_text", search_text)
    displayed_pages = list()
    for page_name in all_pages:
        topic_page = topic_page_manager.get_page_by_name(page_name)
        has_text_matched = search_text in topic_page.content.lower()
        if has_text_matched:
            displayed_pages.append(page_name)

    numb_pages_matched = len(displayed_pages)
    logger.info(f"Number of matched pages: {numb_pages_matched}")
    if numb_pages_matched == 0:
        st.markdown("No matched result found.")
        displayed_pages = [page for page in all_pages]
    else:
        set_variable_in_session_state("displayed_pages", displayed_pages)
elif search_text == "" and search_text != prev_search_text:
    set_variable_in_session_state("search_text", search_text)
    displayed_pages = [page for page in all_pages]
    prev_clicked_button = get_variable_in_session_state("prev_clicked_button")
    cur_clicked_button = get_variable_in_session_state("cur_clicked_button")
    logger.info(f"prev_clicked_button: {prev_clicked_button}")
    logger.info(f"cur_clicked_button: {cur_clicked_button}")

    set_variable_in_session_state("displayed_pages", displayed_pages)
    update_clicked_button_state(get_variable_in_session_state("cur_clicked_button"))

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
        write_horizontal_line()
        st.markdown(page.content, unsafe_allow_html=True)
    else:
        update_clicked_button_state(None)
logger.info("-" * 50)
write_line_break()
write_horizontal_line()
write_markdown_content(icon_markdown_file_path)
