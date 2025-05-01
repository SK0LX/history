import json
import random
import time
from datetime import datetime

from db import get_random_words


class CrosswordGenerator:
    def __init__(self, width, height, word_list, time_limit=5.0, try_second_pass=False):
        self.width = width
        self.height = height
        # Преобразование элементов word_list в кортежи (слово, подсказка), если они строки
        processed_word_list = []
        for w in word_list:
            if isinstance(w, str):
                processed_word_list.append((w, ''))
            else:
                processed_word_list.append((w[0], w[1]))
        # Фильтрация слов, которые являются подстроками других слов
        self.word_list = sorted(
            [w for w in processed_word_list if not any(w[0] != other[0] and w[0] in other[0] for other in processed_word_list)],
            key=lambda x: len(x[0]),
            reverse=True
        )
        self.time_limit = time_limit
        self.try_second_pass = try_second_pass

    def _create_empty_grid(self):
        return [[None for _ in range(self.width)] for _ in range(self.height)]

    def _place_word(self, grid, word, position):
        x, y, direction = position
        dx, dy = (1, 0) if direction == 'H' else (0, 1)
        for letter in word:
            grid[y][x] = letter
            x += dx
            y += dy

    def _valid_position(self, grid, word, x, y, direction):
        dx, dy = (1, 0) if direction == 'H' else (0, 1)
        if x + dx * (len(word)-1) >= self.width or y + dy * (len(word)-1) >= self.height:
            return False
        for letter in word:
            existing = grid[y][x]
            if existing not in (None, letter):
                return False
            if existing is None:
                nx1, ny1 = x + dy, y + dx
                nx2, ny2 = x - dy, y - dx
                for nx, ny in ((nx1, ny1), (nx2, ny2)):
                    if 0 <= nx < self.width and 0 <= ny < self.height and grid[ny][nx] is not None:
                        return False
            x += dx
            y += dy
        return True

    def _score_position(self, grid, word, x, y, direction):
        dx, dy = (1, 0) if direction == 'H' else (0, 1)
        score = 0
        for letter in word:
            if grid[y][x] == letter:
                score += 1
            x += dx
            y += dy
        return score

    def _find_best_positions(self, grid, word):
        candidates = []
        for y in range(self.height):
            for x in range(self.width):
                for direction in ('H', 'V'):
                    if self._valid_position(grid, word, x, y, direction):
                        score = self._score_position(grid, word, x, y, direction)
                        candidates.append(((x, y, direction), score))
        return candidates

    def generate(self):
        best_grid = None
        best_count = -1
        best_placed_info = []
        start_time = time.time()

        while time.time() - start_time < self.time_limit:
            grid = self._create_empty_grid()
            placed_info = []
            placed = 0

            # Размещение первого слова в центре
            if not self.word_list:
                continue
            first_word_info = self.word_list[0]
            first_word = first_word_info[0]
            clue = first_word_info[1]
            dir0 = random.choice(['H', 'V'])
            if dir0 == 'H':
                cx = (self.width - len(first_word)) // 2
                cy = self.height // 2
            else:
                cx = self.width // 2
                cy = (self.height - len(first_word)) // 2
            if self._valid_position(grid, first_word, cx, cy, dir0):
                self._place_word(grid, first_word, (cx, cy, dir0))
                placed_info.append({
                    'word': first_word,
                    'x': cx,
                    'y': cy,
                    'direction': dir0,
                    'clue': clue
                })
                placed += 1
            else:
                continue

            # Размещение остальных слов
            for word_info in self.word_list[1:]:
                word, clue = word_info
                candidates = self._find_best_positions(grid, word)
                if not candidates:
                    continue
                max_score = max(score for _, score in candidates)
                bests = [pos for pos, score in candidates if score == max_score]
                choice = random.choice(bests)
                if max_score == 0:
                    continue
                self._place_word(grid, word, choice)
                placed_info.append({
                    'word': word,
                    'x': choice[0],
                    'y': choice[1],
                    'direction': choice[2],
                    'clue': clue
                })
                placed += 1

            # Второй проход
            if self.try_second_pass:
                for word_info in self.word_list:
                    word, clue = word_info
                    # Пропустить, если слово уже размещено
                    if any(info['word'] == word for info in placed_info):
                        continue
                    candidates = self._find_best_positions(grid, word)
                    if candidates:
                        max_score = max(score for _, score in candidates)
                        bests = [pos for pos, score in candidates if score == max_score]
                        if max_score > 0:
                            choice = random.choice(bests)
                            self._place_word(grid, word, choice)
                            placed_info.append({
                                'word': word,
                                'x': choice[0],
                                'y': choice[1],
                                'direction': choice[2],
                                'clue': clue
                            })
                            placed += 1

            if placed > best_count:
                best_count = placed
                best_grid = [row[:] for row in grid]
                best_placed_info = placed_info.copy()

        return best_grid, best_count, best_placed_info

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(''.join(letter if letter is not None else '#' for letter in row))

    def generate_json(self, filename=None):
        grid, count, placed_info = self.generate()

        # Форматируем данные для JSON
        result = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "width": self.width,
                "height": self.height,
                "total_words": count,
                "attempted_words": len(self.word_list)
            },
            "grid": [[cell or "#" for cell in row] for row in grid],
            "clues": [
                {
                    "word": info['word'],
                    "clue": info['clue'],
                    "x": info['x'] + 1,  # 1-based координаты
                    "y": info['y'] + 1,
                    "direction": "horizontal" if info['direction'] == 'H' else "vertical",
                    "length": len(info['word'])
                }
                for info in placed_info
            ]
        }

        if not filename:
            filename = f"crossword_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        return filename
# Пример использования:
if __name__ == '__main__':
    words = []
    for item in get_random_words():
        words.append((item['word'], item['clue']))
    cg = CrosswordGenerator(15, 15, words, time_limit=5.0, try_second_pass=True)
    output_file = cg.generate_json()
    print(f"Кроссворд сохранён в файл: {output_file}")