import os
import telebot
from AI_tools import _perform_analysis_task as pt
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file; for your safety!
# --- Configuration ---
bot_token = os.getenv("bot_token")

bot = telebot.TeleBot(bot_token,parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Type: SIG [name of cryptocurrency] [timeframe] [limit] [your custom propmt]\nfor example SIG ETH 1h 250 use Al Brooks Method")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Example message from the user
    user_message = message.text
    message_parts = user_message.split()
    checker=message_parts[0].upper()
    if(checker=="SIG"):
        shareName=message_parts[1].upper()
        timeframe=message_parts[2]
        limit = int(message_parts[3])
        user_prompt =str(message_parts[4:])
        symbol=shareName+'/USDT'
        # Print each part separately
        hint,image_path=pt(symbol, timeframe, limit, user_prompt)
        msg=str(hint)
        # Open the image file as binary
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo,msg)
print("Telegram bot starting...")
bot.infinity_polling()

