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


@app.on_message(filters.regex('cply'))
async def playndler(_: Client, message: Message):

    command = message.text.split()

    chat_id = int(command[1])

    replied_message = message.reply_to_message
    if not replied_message or not replied_message.audio:
        await message.reply_text("Reply to an audio message to play it.")
        return

    audio_file_path = f"{replied_message.audio.file_id}.ogg"

    # Download the audio using Pyrogram's download_media
    audioc = await app.download_media(replied_message.audio)
    await message.reply_text(text="Userbot downloaded song")

    try:
        # Play the downloaded audio using PyTG's join_group_call
        await pytg.join_group_call(
            chat_id,
            MediaStream(
                audioc,
                AudioQuality.HIGH,
                video_flags=MediaStream.IGNORE
            ),
        )
    except   AlreadyJoinedError:
       await pytg.leave_group_call(chat_id=message.chat.id)
       await pytg.join_group_call(
            chat_id,
            MediaStream(
                audioc,
                AudioQuality.HIGH,
                video_flags=MediaStream.IGNORE
            ),
        )
    except Exception as e:
        await message.reply_text(f"Error: {e}")