# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/OM64rlU.jpeg

from .. import loader, utils
from telethon.tl.types import Message


@loader.tds
class StickerDownloadMod(loader.Module):
    strings = {
        "name": "StickerDownload",
        "filerr": "<b>😥 Specify a sticker replay to it</b>",
    }
    strings_ru = {"filerr": "<b>😥 Укажи стикер реплаем на него</b>"}

    memes_bot = "@Stickerdownloadbot"
    download_bot = "@Stickerdownloadbot"

    async def on_dlmod(self):
        await utils.dnd(self._client, self.download_bot, True)

    async def stickdowncmd(self, message: Message):
        reply = await message.get_reply_message()
        if not getattr(reply, "sticker", None):
            await utils.answer(message, self.strings("filerr"))
            return

        try:
            async with self._client.conversation(self.download_bot) as conv:
                reply = await message.get_reply_message()
                await conv.send_message(reply)
                phtmem = await conv.get_response()
                await conv.mark_read()
                await message.delete()
                await utils.answer(message, phtmem)
        except ValueError:
            await utils.answer(message, self.strings("filerr"))
