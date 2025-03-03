import re


def get_cleaned_words(source_text):
    """
    returns a list of unique words in a text
    """
    with open(source_text, "r") as file:
        # read file and strip whitespace
        all_lines = file.read().strip()

        # downcase and remove punctuation regex
        cleaned_text = re.sub(r"[^\w\s']", "", all_lines.lower())

        # split into words
        words = cleaned_text.split()
    return words
