# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

from .. import loader, utils

from telethon.tl.types import Message

# meta developer: @shadow_hikka
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/OM64rlU.jpeg


@loader.tds
class RandomMemesMod(loader.Module):
    strings = {"name": "RandomMemes"}
    memes_bot = "@ffmemesbot"

    async def on_dlmod(self):
        await utils.dnd(self._client, self.memes_bot, True)

    async def randmemescmd(self, message: Message):
        async with self._client.conversation(self.memes_bot) as conv:
            await conv.send_message("/start")
            phtmem = await conv.get_response()
            await conv.mark_read()
            await message.delete()
            await utils.answer(message, phtmem)
