# Базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt для установки зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код в контейнер
COPY . /app/

# Задаём переменную окружения для Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Выполняем миграции, собираем статику
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "kittygram_backend.wsgi:application"]

