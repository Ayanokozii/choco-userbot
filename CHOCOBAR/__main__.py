import asyncio
import importlib

from pyrogram import idle

from CHOCOBAR.modules import ALL_MODULES
from pytgcalls import PyTgCalls, idle
loop = asyncio.get_event_loop()


async def initiate_bot():
  for all_module in ALL_MODULES:
    importlib.import_module("CHOCOBAR.modules." + all_module)
    print(f"LOADING {all_module} ...")
  print("Started")
  await idle()
if __name__ == "__main__":
  loop.run_until_complete(initiate_bot())


