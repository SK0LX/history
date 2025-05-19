import json
import random
import time
from datetime import datetime
import logging

from db import get_random_words

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CrosswordGenerator:
    def __init__(self, width, height, word_list, time_limit=5.0, try_second_pass=False):
        self.width = width
        self.height = height
        
        # Проверка входных данных
        if not word_list:
            logger.error("Получен пустой список слов!")
            raise ValueError("Список слов не может быть пустым")

        # Нормализация и фильтрация слов
        processed = []
        for w in word_list:
            if isinstance(w, str):
                processed.append((w.strip().upper(), ''))  # Нормализация регистра
            elif isinstance(w, (list, tuple)) and len(w) >= 1:
                processed.append((w[0].strip().upper(), w[1] if len(w) > 1 else ''))
        
        # Фильтрация слишком длинных слов
        max_possible_length = max(width, height)
        filtered = [
            (word, clue) for word, clue in processed 
            if 0 < len(word) <= max_possible_length
        ]
        
        if not filtered:
            logger.error("Нет подходящих слов после фильтрации!")
            raise ValueError("Нет слов подходящей длины")

        # Упрощенная фильтрация (можно заменить на более сложную логику)
        self.word_list = sorted(
            filtered,
            key=lambda x: (-len(x[0]), x[0]))  # Сортировка по длине и алфавиту

        self.time_limit = time_limit
        self.try_second_pass = try_second_pass
        logger.info(f"Инициализирован генератор с {len(self.word_list)} словами")

    def _create_empty_grid(self):
        return [[None] * self.width for _ in range(self.height)]

    def _place_word(self, grid, word, pos):
        x, y, d = pos
        dx, dy = (1, 0) if d == 'H' else (0, 1)
        for ch in word:
            grid[y][x] = ch
            x += dx; y += dy

    def _valid_position(self, grid, word, x, y, d):
        dx, dy = (1, 0) if d == 'H' else (0, 1)
        # Check word fits
        if x + dx*(len(word)-1) >= self.width or y + dy*(len(word)-1) >= self.height:
            return False
        # Check cell before and after word for buffer
        bx, by = x - dx, y - dy
        ex, ey = x + dx*len(word), y + dy*len(word)
        for cx, cy in ((bx, by), (ex, ey)):
            if 0 <= cx < self.width and 0 <= cy < self.height:
                if grid[cy][cx] is not None:
                    return False
        # Check each letter cell
        cx, cy = x, y
        for ch in word:
            existing = grid[cy][cx]
            if existing not in (None, ch):
                return False
            # Ensure orthogonal neighbors empty
            if existing is None:
                for ox, oy in ((1,0),(-1,0),(0,1),(0,-1)):
                    if ox == dx and oy == dy or ox == -dx and oy == -dy:
                        continue
                    nx, ny = cx+ox, cy+oy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if grid[ny][nx] is not None:
                            return False
            cx += dx; cy += dy
        return True

    def _score_position(self, grid, word, x, y, d):
        dx, dy = (1, 0) if d == 'H' else (0, 1)
        score = 0
        for ch in word:
            if grid[y][x] == ch:
                score += 1
            x += dx; y += dy
        return score

    def _find_best_positions(self, grid, word):
        cand = []
        for y in range(self.height):
            for x in range(self.width):
                for d in ('H','V'):
                    if self._valid_position(grid, word, x, y, d):
                        cand.append(((x,y,d), self._score_position(grid, word, x, y, d)))
        return cand

    def generate(self):
        if not self.word_list:
            logger.error("Попытка генерации без слов!")
            return None, 0, []

        best, best_count, best_info = None, -1, []
        end_time = time.time() + self.time_limit
        
        try:
            # Основная логика генерации
            while time.time() < end_time:
                grid = self._create_empty_grid()
                placed_info = []
                # Place first word centered
                w0, c0 = self.word_list[0]
                d0 = random.choice(('H','V'))
                if d0=='H': x0=(self.width-len(w0))//2; y0=self.height//2
                else: x0=self.width//2; y0=(self.height-len(w0))//2
                if not self._valid_position(grid, w0, x0, y0, d0):
                    continue
                self._place_word(grid, w0, (x0,y0,d0))
                placed_info.append({'word':w0,'x':x0,'y':y0,'d':d0,'clue':c0})
                # Place remaining words
                for w, clue in self.word_list[1:]:
                    poss = self._find_best_positions(grid, w)
                    if not poss: continue
                    max_s = max(s for _,s in poss)
                    if max_s<=0: continue
                    bests = [p for p,s in poss if s==max_s]
                    choice = random.choice(bests)
                    self._place_word(grid, w, choice)
                    placed_info.append({'word':w,'x':choice[0],'y':choice[1],'d':choice[2],'clue':clue})
                # Second pass
                if self.try_second_pass:
                    for w, clue in self.word_list:
                        if any(i['word']==w for i in placed_info): continue
                        poss = self._find_best_positions(grid, w)
                        if not poss: continue
                        max_s = max(s for _,s in poss)
                        if max_s<=0: continue
                        choice = random.choice([p for p,s in poss if s==max_s])
                        self._place_word(grid, w, choice)
                        placed_info.append({'word':w,'x':choice[0],'y':choice[1],'d':choice[2],'clue':clue})
                if len(placed_info) > best_count:
                    best_count = len(placed_info)
                    best = [row[:] for row in grid]
                    best_info = list(placed_info)
        except Exception as e:
            logger.error(f"Ошибка генерации: {str(e)}")
            return None, 0, []

        return best, best_count, best_info

    def generate_json(self):
        grid, count, info = self.generate()
        res = {
            'metadata':{
                'generated_at':datetime.now().isoformat(),
                'width':self.width,'height':self.height,
                'total_words':count,'attempted_words':len(self.word_list)
            },
            'grid':[[cell or '#' for cell in row] for row in grid],
            'clues':[]
        }
        for i in info:
            res['clues'].append({
                'word':i['word'],'clue':i['clue'],
                'x':i['x']+1,'y':i['y']+1,
                'direction':'horizontal' if i['d']=='H' else 'vertical',
                'length':len(i['word'])
            })
        return res

if __name__ == '__main__':
    words = [(item['word'], item['clue']) for item in get_random_words()]
    cg = CrosswordGenerator(15, 15, words, time_limit=5.0, try_second_pass=True)
    # Generate JSON and extract the grid
    result = cg.generate_json()
    grid = result['grid']  # list of lists with letters and '#'
    print(result)
    # Print the crossword in console
    for row in grid:
        print(''.join(cell.replace("#", " ") for cell in row))

    print(f"\nTotal words placed: {result['metadata']['total_words']}")
