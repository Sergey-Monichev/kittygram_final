# Kittygram - Финальное задание

![CI/CD](https://github.com/Sergey-Monichev/kittygram_final/actions/workflows/kittygram_workflow.yml/badge.svg)

## Описание проекта
Kittygram — это веб-приложение для управления базой данных о кошках. Оно поддерживает добавление, редактирование и просмотр информации о питомцах, а также управление достижениями.

Проект разворачивается в контейнерах Docker и использует CI/CD для автоматизированного тестирования и деплоя на сервер.

## Используемые технологии
- Python 3.9
- Django REST Framework
- PostgreSQL
- Docker и Docker Compose
- Nginx
- Gunicorn
- GitHub Actions (CI/CD)

## Как развернуть проект

### 1. Клонирование репозитория
```bash
git clone https://github.com/Sergey-Monichev/kittygram_final.git
cd kittygram_final
```

### 2. Создание .env файла
Создайте файл `.env` в корневой директории и укажите в нем следующие переменные:
```env
DJANGO_SECRET_KEY=supersecretkey
DEBUG=False
ALLOWED_HOSTS=kittygram-example.hopto.org,localhost,127.0.0.1
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
DB_HOST=db
DB_PORT=5432
```

### 3. Сборка и запуск контейнеров
```bash
docker-compose -f docker-compose.production.yml up --build -d
```

### 4. Выполнение миграций и сбор статики
```bash
docker-compose -f docker-compose.production.yml exec backend python manage.py migrate
docker-compose -f docker-compose.production.yml exec backend python manage.py collectstatic --no-input
```

### 5. Проверка работы
Откройте браузер и перейдите по адресу:
```
http://kittygram-example.hopto.org
```

## Как проверить работу с помощью автотестов

1. Создайте файл `tests.yml` в корне репозитория со следующим содержимым:
```yaml
repo_owner: ваш_логин_на_гитхабе
kittygram_domain: https://kittygram-example.hopto.org
taski_domain: https://taski-example.hopto.org
dockerhub_username: ваш_логин_на_докерхабе
```

2. Скопируйте содержимое `.github/workflows/main.yml` в файл `kittygram_workflow.yml` в корневой директории проекта.

3. Запустите тесты локально:
```bash
pytest
```

## Чек-лист перед отправкой задания

- Проект Taski доступен по доменному имени, указанному в `tests.yml`.
- Проект Kittygram доступен по доменному имени, указанному в `tests.yml`.
- Пуш в ветку main запускает тестирование и деплой Kittygram, а после успешного деплоя вам приходит сообщение в телеграм.
- В корне проекта есть файл `kittygram_workflow.yml`.

## Автор нов
**Сергей Моничев**  
GitHub: [Sergey-Monichev](https://github.com/Sergey-Monichev/)
Test1