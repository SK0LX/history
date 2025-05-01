from flask import Flask, jsonify
import random, psycopg2

app = Flask(__name__)

# Настройки подключения к БД
DB_CONFIG = {
    'dbname': 'crossword_db',
    'user': 'user',
    'password': 'pass',
    'host': 'localhost'
}

def get_random_pair():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT word1, word2, clue1, clue2 FROM pairs ORDER BY RANDOM() LIMIT 1;")
    row = cur.fetchone()
    cur.close(); conn.close()
    return row  # (word1, word2, clue1, clue2)

def build_crossword(w1, w2):
    # Найти общее пересечение
    for i, ch1 in enumerate(w1):
        for j, ch2 in enumerate(w2):
            if ch1 == ch2:
                ix1, ix2 = i, j
                break
        else:
            continue
        break
    else:
        # Если нет общих букв — просто выводим оба слова по горизонтали
        return {
            'rows': [
                list(w1),
                list(w2)
            ]
        }

    # Вычисляем размеры сетки
    top = ix2
    bottom = len(w2) - ix2 - 1
    left = 0
    right = len(w1) - ix1 - 1
    height = top + 1 + bottom
    width  = left + 1 + right

    # Инициализируем сетку пустыми строками
    grid = [['' for _ in range(width)] for __ in range(height)]

    # Кладём word1 горизонтально в row = top, col 0..len(w1)-1
    for k, ch in enumerate(w1):
        grid[top][k] = ch.upper()

    # Кладём word2 вертикально так, чтобы пересечение совпало
    for k, ch in enumerate(w2):
        row = k
        col = ix1
        grid[row][col] = ch.upper()

    return {
        'rows': grid
    }

@app.route('/api/crossword')
def api_crossword():
    w1, w2, clue1, clue2 = get_random_pair()
    crossword = build_crossword(w1.strip(), w2.strip())
    return jsonify({
        'word1': w1,
        'word2': w2,
        'clue1': clue1,
        'clue2': clue2,
        'grid': crossword['rows']
    })

if __name__ == '__main__':
    app.run(debug=True)
