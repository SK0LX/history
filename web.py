from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from Crossword import CrosswordGenerator
from db import get_random_words

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


@app.route('/crossword', methods=['GET'])
def generate_crossword():
    words = [(item['word'], item['clue']) for item in get_random_words()]
    crossword = CrosswordGenerator(15, 15, words, time_limit=5.0, try_second_pass=True)
    return jsonify(crossword.generate_json())

if __name__ == '__main__':
    app.run(debug=True)