import os
from typing import List

API_ID = os.environ.get("API_ID", "35057086")
API_HASH = os.environ.get("API_HASH", "344c241bb482993a8b318848421319f3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8605427721:AAHeo63F4QU9rA1Jdph6yhDOCVEbG0dQeNQ")
ADMIN = int(os.environ.get("ADMIN", "7811733658"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001301597448"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Sanjay20022:Sanjay@20022@cluster0.btgw8dj.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1001301597448").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
