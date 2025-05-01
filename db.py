import psycopg2
import random

def get_random_words():
    try:
        # Подключение к PostgreSQL (замените параметры на свои)
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Lfybbk_2005"
        )

        # Создаем курсор
        with conn.cursor() as cursor:
            # Генерируем SQL-запрос
            query = """
            WITH random_limit AS (
                SELECT floor(random() * 9 + 12)::int AS limit_value
            )
            SELECT word, clue 
            FROM words
            ORDER BY random()
            LIMIT (SELECT limit_value FROM random_limit);
            """

            # Выполняем запрос
            cursor.execute(query)

            # Получаем результаты
            results = cursor.fetchall()

            # Преобразуем в список словарей
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in results]

    except Exception as e:
        print(f"Ошибка: {e}")
        return []
    finally:
        if conn:
            conn.close()
