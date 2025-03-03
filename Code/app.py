"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram
from markov_chain import MarkovChain
from helpers import get_cleaned_words


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
word_list = get_cleaned_words("metamorphosis.txt")

# word_list = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!".split()
# histogram = Dictogram(word_list)
markov_chain = MarkovChain(word_list)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # random_word = histogram.sample()
    random_sentence = markov_chain.random_walk()
    return "<p>Random Sentence: {}</p>".format(random_sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
    To learn more about Flask's DEBUG mode, visit
    https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
