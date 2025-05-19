import os
import random
from venv import logger

import psycopg2
from psycopg2 import sql

# Глобальная переменная для кэширования всех слов из БД
_cached_words = None

def get_random_words(limit=50):
    """Возвращает случайные слова из кэшированного списка."""
    global _cached_words
    
    # Загружаем слова при первом вызове
    if _cached_words is None:
        _cached_words = _load_all_words_from_db()
    
    # Если список слов пуст или загрузка не удалась
    if not _cached_words:
        return []
    
    # Выбираем случайные слова из кэша
    sample_size = min(limit, len(_cached_words))
    return random.sample(_cached_words, sample_size)

def _load_all_words_from_db():
    """Загружает все слова из базы данных и возвращает список."""
    conn = None
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("DB_HOST", "db"),
            port=os.getenv("DB_PORT", "5432")
        )
        
        # Получаем все записи из таблицы
        with conn.cursor() as cur:
            cur.execute(sql.SQL("SELECT word, clue FROM words"))
            return [
                {"word": row[0], "clue": row[1]}
                for row in cur.fetchall()
            ]
    
    except Exception as e:
        logger.error(f"Ошибка загрузки слов: {str(e)}")
        return None  # Ошибка загрузки
    
    finally:
        if conn is not None:
            conn.close()
