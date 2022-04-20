"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
import telethon
from telethon import TelegramClient

# scope: meta developer: @shadow_geektg

@loader.tds
class RandomMemesMod(loader.Module):
    strings = {"name": "RandomMemes"}
    """Random memes"""
    async def client_ready(self, client: TelegramClient, db):
        self.memes_bot = "@ffmemesbot"
        self._db = db
        self._client = client
    
    async def randmemescmd(self, message: Message) -> None:
        """Send random memes"""
        async with self._client.conversation(self.memes_bot) as conv:
            mem = await conv.send_message("/start")
            phtmem = await conv.get_response()
            await conv.mark_read()
            await message.delete()
            await utils.answer(message, phtmem)
