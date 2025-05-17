import os
import psycopg2
import random

def get_random_words():
    url = os.getenv('DATABASE_URL',
                    'postgresql://postgres:postgres@db:5432/postgres')
    try:
        conn = psycopg2.connect(url)
        with conn.cursor() as cursor:
            query = """
            WITH random_limit AS (
                SELECT floor(random() * 9 + 12)::int AS limit_value
            )
            SELECT word, clue 
            FROM words
            ORDER BY random()
            LIMIT (SELECT limit_value FROM random_limit);
            """
            cursor.execute(query)
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in results]
    except Exception as e:
        print(f"Ошибка: {e}")
        return []
    finally:
        if conn:
            conn.close()
