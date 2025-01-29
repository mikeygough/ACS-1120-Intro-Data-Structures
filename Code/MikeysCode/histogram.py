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


def generate_histogram(cleaned_words):
    """
    returns a histogram of the unique words in a text
    """
    histogram = {}
    for word in cleaned_words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram


def unique_words(histogram):
    """
    returns the total count of unique words in the histogram
    """
    return len(histogram)


def frequency(word, histogram):
    """
    returns the number of times that word appears in a histogram
    """
    count = histogram.get(word, 0)
    if count == 0:
        print(f"'{word}' not in histogram")
    return count


if __name__ == "__main__":
    cleaned_words = get_cleaned_words("metamorphosis.txt")
    histogram = generate_histogram(cleaned_words)
    print(histogram)
    print(unique_words(histogram))
    print(frequency("test", histogram))
