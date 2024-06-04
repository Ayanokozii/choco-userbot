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






@app.on_message(filters.regex('play') & filters.user(OWNER_ID))
async def play_handler(_, message):
  replied_message = message.reply_to_message

  if not replied_message or  not (replied_message.audio or replied_message.video):
    await message.reply_text("Reply to an audio message to play it.")
    return 
  audio_file_path = None
  
  if replied_message.audio:
     audio_file_path = f"{replied_message.audio.file_id}.ogg"
  elif replied_message.video:
     audio_file_path = f"{replied_message.video.file_id}.ogg"
  media = await app.download_media(replied_message)
  await message.reply_text(text="Userbot  downloaded Media")
  await pytg.join_group_call(
      message.chat.id,
      MediaStream(media,AudioQuality.HIGH,VideoQuality.HD_720p,),
  )




@app.on_message(filters.regex('.pause'))
async def pause_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  paused song")
  await pytg.pause_stream(message.chat.id, )


@app.on_message(filters.regex('.stop'))
async def stop_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  stopped song.")
  await pytg.leave_group_call(message.chat.id, )


@app.on_message(filters.regex('.resume'))
async def resume_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  resume song")
  await pytg.resume_stream(message.chat.id, )
