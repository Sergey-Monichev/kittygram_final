# Используем базовый образ Nginx
FROM nginx:1.22.1

# Копируем файл конфигурации Nginx в контейнер
COPY nginx.conf /etc/nginx/templates/default.conf.template

# Устанавливаем рабочую директорию (опционально, для ясности)
WORKDIR /etc/nginx

# Открываем порт 80 для взаимодействия с сервером
EXPOSE 80
