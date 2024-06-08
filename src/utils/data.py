import os


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
