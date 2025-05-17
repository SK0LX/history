import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from Crossword import CrosswordGenerator
from db import get_random_words

# Абсолютный путь до папки frontend
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, '..', 'frontend')

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,   # именно оттуда будем раздавать статику
    static_url_path=''             # корневой URL → папка frontend
)
CORS(app)

# 1) API-маршрут ОБЯЗАТЕЛЬНО первым
@app.route('/crossword', methods=['GET'])
def generate_crossword():
    words = [(item['word'], item['clue']) for item in get_random_words()]
    crossword = CrosswordGenerator(15, 15, words,
                                  time_limit=5.0,
                                  try_second_pass=True)
    return jsonify(crossword.generate_json())

# 2) Корень сайта — отдадим index.html
@app.route('/')
def index():
    return app.send_static_file('index.html')

# 3) Любые остальные файлы (.js, .css, картинки…) тоже из frontend
# Flask сам разрулит, так как static_url_path=''
# Но можно явно:
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

if __name__ == '__main__':
    # слушаем на всех интерфейсах 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
