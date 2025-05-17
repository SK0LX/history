# 1. Базовый образ с Python
FROM python:3.11.9-slim

# 2. Системные пакеты для psycopg2 (если вы его используете)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 3. Рабочая директория
WORKDIR /app

# 4. Копируем и ставим Python-зависимости
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь проект
COPY backend/ ./backend
COPY frontend/ ./frontend

# 6. Перенастраиваем Flask:  
#    пусть web.py в backend импортирует статику из ../frontend
WORKDIR /app/backend

# 7. Открываем порт (Flask по умолчанию 5000)
EXPOSE 5000

# 8. Запуск
CMD ["python", "web.py"]
