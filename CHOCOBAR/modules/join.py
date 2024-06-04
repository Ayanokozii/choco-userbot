import os
from pyrogram import filters
from pyrogram.types import Message
from CHOCOBAR import app, pytg
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
from config import OWNER_ID
# OWNER_ID = 6621610889
@app.on_message(filters.regex("join") & filters.user(OWNER_ID))
async def join(client, message):
         commands = message.text.split(maxsplit=1)
         if  len(commands) != 2:
           await message.reply_text("invalid command")
         print(commands)
         chat_id = commands[1]
         await pytg.join_group_call(chat_id,MediaStream("https://github.com/anars/blank-audio/blob/master/10-seconds-of-silence.mp3",AudioQuality.HIGH,
          video_flags=MediaStream.IGNORE),)
