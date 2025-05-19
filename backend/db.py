import os
from venv import logger

import psycopg2
import random

from psycopg2 import sql


def get_random_words(limit=50):
    """Получаем случайные слова из базы данных"""
    conn = None  # Инициализируем переменную
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host=os.getenv("DB_HOST", "db"),
            port=os.getenv("DB_PORT", "5432")
        )

        # Выполняем запрос
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT word, clue 
                FROM words 
                ORDER BY RANDOM() 
                LIMIT %s
            """)
            cur.execute(query, (limit,))

            result = [
                {"word": row[0], "clue": row[1]}
                for row in cur.fetchall()
            ]

        return result

    except Exception as e:
        logger.error(f"Ошибка при запросе к БД: {str(e)}")
        return []

    finally:
        # Всегда закрываем соединение, если оно было открыто
        if conn is not None:
            conn.close()
