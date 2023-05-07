import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6219828328:AAHMCXKivSPCnPwD0HhF5TVolcM6d0kj2Ss")
API_ID = int(os.environ.get("API_ID", "9307118"))

API_HASH = os.environ.get("API_HASH", "be05f79c70a53f39abbcc009de3450f3")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
