import os
import logging
from pyrogram import Client, filters

# Налаштування логування
logging.basicConfig(level=logging.INFO)  # Встановлення рівня логування
logger = logging.getLogger(__name__)  # Отримання логера

# Введіть ваші дані з середовища
API_ID = os.getenv("API_ID")  # Введіть ваш API ID (в середовищі)
API_HASH = os.getenv("API_HASH")  # Введіть ваш API Hash (в середовищі)
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Введіть токен бота (в середовищі)

# Ініціалізація бота
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.new_chat_members)  # Обробка нових учасників
async def new_member(client, message):
    logger.info("Новий учасник приєднався до чату.")
    await message.delete()  # Видалення повідомлення

@app.on_message(filters.left_chat_member)  # Обробка учасників, які залишили чат
async def left_member(client, message):
    logger.info("Учасник залишив чат.")
    await message.delete()  # Видалення повідомлення

if __name__ == "__main__":
    logger.info("Запуск бота...")
    app.run()
    logger.info("Бот зупинений.")
