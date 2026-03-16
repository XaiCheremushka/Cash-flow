# Веб-сервис для управления движением денежных средств (ДДС) "Cash Flow"

**ДДС (движение денежных средств)** — это процесс учета, управления и анализа поступлений и списаний денежных средств компании или частного лица.

---

## БД 

![Untitled](https://github.com/user-attachments/assets/c2271ae5-c2f5-4bf3-9cc9-0359479663a5)

---
# Технологии

- **Backend:** Python 3.13, Django, Django REST Framework
- **База данных:** PostgreSQL
- **Сервер:** Gunicorn, Nginx
- **Контейнеризация:** Docker, Docker Compose

---
## Инструкция по запуску проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/XaiCheremushka/Cash-flow
```
### 2. Настройка переменных окружения
#### Создайте файл .env в корне проекта и заполните его по примеру из .env_example. Данные для примера:
```dotenv
# Project
SECRET_KEY=django-insecure-&39a22uip68)k36m&x64fd3#s8p*=*8*xq)=ero4c^!*kjqryd
ALLOWED_HOSTS=localhost
SITE_HOST=cashflow
SITE_PORT=8000

# Database
DATABASE_NAME=cashflow_db
DATABASE_USER=cashflow_user
DATABASE_PASSWORD=cashflow_password
DATABASE_HOST=postgres
DATABASE_PORT=5432
```
### 3. Запуск проекта с помощью Docker Compose:
#### Запустите Docker Desktop
#### Запуск и сборка проекта из корня проекта (рядом с файлом docker-compose.yml):
```bash
docker compose up -d --build
```
### 4. Создание суперпользователя
#### Войдите в контейнер с приложением:
```bash
docker compose exec cashflow_server bash
```
#### Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
#### Введите данные (можно любые другие):
Username: root

Email: (можно оставить пустым)

Password: root

Password (again): root

#### Согласитесь с тем, чтобы создать пользователя в любом случае: 
```bash
y
```

#### Выйдите из контейнера:
```bash
exit
```

### 5. Проверка работоспособности
#### После запуска проект будет доступен:

Админ-панель: http://localhost/admin (логин: root, пароль: root)
Swagger-документация к API: http://localhost/api/v1/schema/swagger-ui/

### 6. Выключение контейнеров:
```bash
docker compose down
```
