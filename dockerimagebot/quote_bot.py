import logging
import random
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_quotes():
    quotes_file_path = '/app/quotes.txt'
    with open(quotes_file_path, 'r', encoding='utf-8') as f:
        return [quote.strip() for quote in f.readlines()]

# Загрузка цитат из файла
quotes = load_quotes()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот-цитатник. Напиши /quote, чтобы получить случайную цитату')

# Команда /quote
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_quote = random.choice(quotes)
    await update.message.reply_text(random_quote)

# Основная функция для запуска бота
if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quote", quote))

    # Запуск бота
    application.run_polling()