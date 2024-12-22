# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости для PostgreSQL и системы
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта
COPY . .

# Переменные окружения (из файла .env)
ENV PYTHONUNBUFFERED=1

# Собираем статику
RUN python manage.py collectstatic --no-input

# Открываем порт для работы с сервером
EXPOSE 8000

# Команда запуска приложения через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi:application"]
