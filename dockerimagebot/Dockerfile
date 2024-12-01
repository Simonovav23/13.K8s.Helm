# Этап сборки
FROM python:3.11-slim AS builder

WORKDIR /app

# Установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Этап финального образа
FROM python:3.11-slim

WORKDIR /app

# Копируем установленные зависимости
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app .

# Команда по умолчанию
CMD ["python", "quote_bot.py"]