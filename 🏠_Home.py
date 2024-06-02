import streamlit as st
from src.st.utils import (
    load_yaml,
    generate_topic_pages_info_list_from_pages_folder,
    display_topic_shortcuts,
    write_line_break,
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
page_name_to_topic_page_map, topic_page_list = (
    generate_topic_pages_info_list_from_pages_folder()
)
if "page_name_to_topic_page_map" not in st.session_state:
    st.session_state.page_name_to_topic_page_map = page_name_to_topic_page_map

# ### PAGE CONTENT
st.title("Knowledge Vault")
intro = """
---
Welcome to **Knowledge Vault** - my personal library of knowledge, providing a reference point for my own learning journey 
in Machine Learning and Software Engineering.

It's a space to explore, discover, and reflect on the concepts and techniques I have learned along the way.

---
"""
st.markdown(intro)

st.markdown("Topic shortcuts")
topic_page_is_clicked_dict = display_topic_shortcuts(topic_page_list)
for topic_page, is_clicked in topic_page_is_clicked_dict.items():
    if is_clicked:
        st.switch_page(topic_page.url)

write_line_break(numb_lines=1)
search_text = st.text_input("Enter your search query:")

if search_text != "":
    st.markdown("Feature is not available yet.")


# import streamlit as st


# # Define subpages as functions
# def home():
#     st.title("Home Page")
#     st.write("Welcome to the home page!")


# def about():
#     st.title("About Page")
#     st.write("Welcome to the about page!")


# def contact():
#     st.title("Contact Page")
#     st.write("Welcome to the contact page!")


# # Mapping of subpage names to functions
# pages = {
#     "Home": home,
#     "About": about,
#     "Contact": contact,
# }


# # Function to handle navigation
# def navigate():
#     query_params = st.experimental_get_query_params()
#     subpage = query_params.get("subpage", ["Home"])[0]

#     if subpage in pages:
#         st.session_state.current_page = subpage
#     else:
#         st.session_state.current_page = "Home"

#     # Render the selected subpage
#     pages[st.session_state.current_page]()


# # Sidebar for navigation
# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(pages.keys()), key="nav")

# # Set the query parameters based on the sidebar selection
# st.experimental_set_query_params(subpage=selection)

# # Handle navigation
# navigate()

# # Display the current subpage
# st.sidebar.write(f"Current page: {st.session_state.current_page}")
