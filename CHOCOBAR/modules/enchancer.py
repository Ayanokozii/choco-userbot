import base64
import hashlib
import httpx
from pyrogram import Client, filters
import asyncio
import os
from CHOCOBAR import app
from  pyrogram.types import Message 
API_KEY = "CH3TraChW9dJx4X7Bl3LjtCBn1GQv8EXTYBAdjsQKyOQ1YRF"

# Define the path to the temporary image folder
IMAGE_FOLDER = "./img_temp/"
# Ensure the folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Change this accordingly
CONTENT_TYPE = "image/jpeg"
OUTPUT_CONTENT_TYPE = "image/jpeg"

_TIMEOUT = 60
_BASE_URL = "https://developer.remini.ai/api"


def _get_image_md5_content(image_path: str) -> tuple[str, bytes]:
    with open(image_path, "rb") as fp:
        content = fp.read()
        image_md5 = base64.b64encode(hashlib.md5(content).digest()).decode("utf-8")
    return image_md5, content


async def process_media(client, message):
    # Ensure the message contains media
    if message.media:
        # Download the media to the temporary folder
        media_path = os.path.join(IMAGE_FOLDER, "downloaded_image.jpg")
        await client.download_media(message, file_name=media_path)

        # Get the MD5 hash and content of the downloaded image
        image_md5, content = _get_image_md5_content(media_path)

        # Setup an HTTP client with the correct options
        async with httpx.AsyncClient(
            base_url=_BASE_URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
        ) as http_client:
            # Submit the task
            response = await http_client.post(
                "/tasks",
                json={
                    "tools": [
                        {"type": "face_enhance", "mode": "beautify"},
                        {"type": "background_enhance", "mode": "base"},
                    ],
                    "image_md5": image_md5,
                    "image_content_type": CONTENT_TYPE,
                    "output_content_type": OUTPUT_CONTENT_TYPE,
                },
            )
            assert response.status_code == 200
            body = response.json()
            task_id = body["task_id"]

            # Upload the image
            response = await http_client.put(
                body["upload_url"], headers=body["upload_headers"], content=content, timeout=_TIMEOUT
            )
            assert response.status_code == 200

            # Process the image
            response = await http_client.post(f"/tasks/{task_id}/process")
            assert response.status_code == 202

            # Get the image
            for _ in range(50):
                response = await http_client.get(f"/tasks/{task_id}")
                assert response.status_code == 200

                if response.json()["status"] == "completed":
                    break
                else:
                    await asyncio.sleep(2)

            # Send the enhanced image to the user who sent the command
            await client.send_photo(
                message.chat.id,
                response.json()["result"]["output_url"],
                reply_to_message_id=message.message_id,
            )


# Define a command handler for the /enc command
@app.on_message(filters.command("enc"))
async def encrypt_image(client, message):
    # Ensure there's a replied-to message
    if message.reply_to_message and message.reply_to_message.media:
        # Forward the replied-to message to the process_media function
        await process_media(client, message.reply_to_message)

