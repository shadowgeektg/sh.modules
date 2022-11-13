# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# meta banner: https://i.imgur.com/OM64rlU.jpeg

from .. import loader, utils
from telethon.tl.types import Message  # type: ignore
import random


@loader.tds
class VulgarStories(loader.Module):
    strings = {
        "name": "VulgarStories",
        "warning": "⛔️ <b>I do not recommend using this module.</b>\n🍆 <b>In many chat rooms, all sorts of vulgar stories are prohibited.</b>",
    }
    strings_ru = {
        "warning": "⛔️ <b>Не советую использовать этот модуль</b>\n🍆 <b>Во многих чатах запрещены всякие пошлые истории</b>",
    }

    async def client_ready(self):
        self.messages = random.choice(
            await self.client.get_messages("pirsikowe", limit=100)
        )
        if not self.get("warning_stories", False):
            await self.inline.bot.send_message(
                self._tg_id,
                text=self.strings("warning"),
            )
        self.set("warning_stories", True)

    async def vstorcmd(self, message: Message):
        """Vulgar Stories for gays."""
        await utils.answer(message, self.persik)
