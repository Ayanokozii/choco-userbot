import os
from gtts import gTTS
from CHOCOBAR import app, pytg
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream

@app.on_message(filters.regex('pts'))
async def playr(_, message: Message):
    command = message.text.split()

    # Extract the text from the command
    text = ' '.join(command[1:])  # Joining text after the command

    # Convert text to speech using gTTS
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save('output.mp3')
    media="output.mp3"
    chat_id = message.chat.id
    # Play the speech in the group call
    await pytg.join_group_call(
        chat_id,
        MediaStream(media,AudioQuality.HIGH,video_flags=MediaStream.IGNORE),
    )
