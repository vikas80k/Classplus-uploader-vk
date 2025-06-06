#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23634056"))
API_HASH = environ.get("API_HASH", "f2debf49c2f57bad88086ecd17cb5df3")
BOT_TOKEN = environ.get("BOT_TOKEN", "7838647960:AAFV_c63_j4Afs_IrH9B0QMVGYIczwGEzHk")
OWNER = int(environ.get("OWNER", "5082207960"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5082207960').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
