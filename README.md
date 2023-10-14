# adopt-me-api-django-celery

Инструкция по запуску:
1) Создать виртуальное окружение командой - "python -m venv .venv"
2) Активировать виртуальное окружение - ".venv/scripts/activate" (для Windows)
3) Установить все необходимые зависимости с помощью команды - "pip install -r requirements.txt"
4) Создать .env файл в главной директории, задать в нём 3 переменные в следующем виде:
 - PROJECT_NAME = "send_mate" 
 - API_ADDRESS = 'https://probe.fbrq.cloud/v1' 
 - AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc3ODc1MDMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9IZWxsb3VIb3UifQ.mfj7Q5dS6A4RBl0e74kqmfx5dJlXcjIWZfKMksGYteY"
Или заменить токен на свой собственный 
5) Запустить django с помощью команды - "python manage.py runserver"
6) Включить Redis открыв папку с одноимённым названием в главной директории, и запустив файл с названием "redis-server"
7) Запустить celery командой - "celery -A send_mate.celery worker --pool=solo -l info"

Документация по API: 
-Путь к роутеру: -http://127.0.0.1:8000/api/
-Клиенты: http://127.0.0.1:8000/api/clients
 -Конкретный клиент: http://127.0.0.1:8000/api/clients/{id}
-Рассылки: http://127.0.0.1:8000/api/newsletters
 -Конкретная рассылка: http://127.0.0.1:8000/api/newsletters/{id}
-Сообщения: http://127.0.0.1:8000/api/messages
 --Конкретное сообщение: http://127.0.0.1:8000/api/messages/{id}