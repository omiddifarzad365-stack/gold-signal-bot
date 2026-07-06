import requests
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID, API_KEY

print("Starting Gold Signal Bot...")

# تست اتصال به Twelve Data
url = f"https://api.twelvedata.com/time_series?symbol=XAU/USD&interval=5min&outputsize=1&apikey={API_KEY}"

response = requests.get(url)

print("Twelve Data Status:", response.status_code)
print(response.text)

# تست ارسال پیام تلگرام
bot = Bot(BOT_TOKEN)

bot.send_message(
    chat_id=CHAT_ID,
    text="✅ Gold Signal Bot is Online"
)

print("Done")
