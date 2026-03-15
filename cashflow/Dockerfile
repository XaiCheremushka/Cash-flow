FROM python:3.13-slim

# Фиксированные UID/GID (ВАЖНО)
ARG UID=1001
ARG GID=1001

# Создаем пользователя внутри контейнера в Debian и присваиваем ему id для последующего получаения доступа к томам
RUN groupadd -g ${GID} groupDjangoCashFlow && \
    useradd -u ${UID} -g ${GID} -m userCashFlowDj

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Прописываем команды для создания зависимостей при сборке образа
# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем и переходим в рабочую директорию
WORKDIR /app/www/cashflow

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем ВЕСЬ проект
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER userCashFlowDj
