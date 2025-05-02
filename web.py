from flask import Flask, jsonify
import random

from Crossword import CrosswordGenerator
from db import get_random_words

app = Flask(__name__)

@app.route('/crossword', methods=['GET'])
def generate_crossword():
    words = []
    for item in get_random_words():
        words.append((item['word'], item['clue']))
    Crossword = CrosswordGenerator(15, 15, words, time_limit=5.0, try_second_pass=True)
    return jsonify(Crossword.generate_json())

if __name__ == '__main__':
    app.run(debug=True)
