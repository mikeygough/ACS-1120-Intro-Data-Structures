"""Main script, uses other modules to generate sentences."""

from flask import Flask, render_template_string

# from dictogram import Dictogram
# from markov_chain import MarkovChain
from nth_order_markov_chain import NthOrderMarkovChain
from helpers import get_cleaned_words


app = Flask(__name__)

word_list = get_cleaned_words("metamorphosis.txt")
markov_chain = NthOrderMarkovChain(word_list, order=3)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    random_sentence = markov_chain.random_walk(101)
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Sentence Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
            }
            .sentence {
                font-size: 1.5em;
                color: #333;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            .source {
                font-size: 0.9em;
                color: #666;
                margin-top: 10px;
                font-style: italic;
            }
            .refresh {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .refresh:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Random Sentence Generator</h1>
            <p class="sentence">Random Sentence: {{ sentence }}</p>
            <p class="source">Source: Metamorphosis by Franz Kafka</p>    
            <a href="/" class="refresh">Generate New Sentence</a>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, sentence=random_sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
    To learn more about Flask's DEBUG mode, visit
    https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
