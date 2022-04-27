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

# scope: meta developer: @shadow_hikka

@loader.tds
class StickerDownloadMod(loader.Module):
    strings = {"name": "StickerDownload", "filerr": "<b>😥 Specify a sticker replay to it</b>"}
    strings_ru = {"filerr": "<b>😥 Укажи стикер реплаем на него</b>"}
    
    memes_bot = "@Stickerdownloadbot"

    async def client_ready(self, client: TelegramClient, db):
        self.memes_bot = "@Stickerdownloadbot"
        self._db = db
        self._client = client

    async def on_dlmod(self, client: "TelegramClient", db: "database.Database"):
        await utils.dnd(client, self.memes_bot, True)
    
    async def stickdowncmd(self, message: Message) -> None:
        try:
            async with self._client.conversation(self.memes_bot) as conv:
                reply = await message.get_reply_message()
                mem = await conv.send_message(reply)
                phtmem = await conv.get_response()
                await conv.mark_read()
                await message.delete()
                await utils.answer(message, phtmem)
        except ValueError:
            await utils.answer(message, self.strings("filerr"))