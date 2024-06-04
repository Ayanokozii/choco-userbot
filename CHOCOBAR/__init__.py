import asyncio
import time

from pyrogram import Client
from pyrogram.methods.utilities import idle
from pyrogram.types import Message
import config
from pytgcalls import PyTgCalls, idle

loop = asyncio.get_event_loop()
boot = time.time()

app = Client(
    ":CHOCOBAR:",
    config.API_ID,
    config.API_HASH,
    session_string=config.SESSION,
)  

pytg = PyTgCalls(app)



async def initiate_bot():
  global app
  await pytg.start()

loop.run_until_complete(initiate_bot())
