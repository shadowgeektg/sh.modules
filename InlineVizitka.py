"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
import logging
import asyncio

# scope: hikka_only
# meta developer: @shadow_geektg, @dan_endy, @hikariatama

logger = logging.getLogger(__name__)


@loader.tds
class InlineVizitkaMod(loader.Module):
    strings = {
        "name": "InlineVizitka",
        "mysocial": "<b>✨ My social networks</b>",
        "clickvk": "🦚 VK",
        "httpserr": "<b>❗ Warning ❗\nThe link must start with</b> <code>https://</code>",
        "novk": "<b>😰 You didn't enter your VK</b>",
        "nodis": "<b>🌧 You didn't enter your discord</b>",
        "notwit": "<b>🛑 You didn't enter your twitter</b>",
        "noinst": "<b>😥 You didn't enter your instagram</b>",
        "lnknotset": "❌ Link not set",
    }

    strings_ru = {
        "mysocial": "<b>✨ Мои соцсети</b>",
        "clickvk": "🦚 VK",
        "httpserr": "<b>❗ Предупреждение ❗\nСсылка должна начинаться на</b> <code>https://</code>",
        "novk": "<b>😰 Вы не ввели свой VK</b>",
        "nodis": "<b>🌧 Вы не ввели свой discord</b>",
        "notwit": "<b>🛑 Вы не ввели свой twitter</b>",
        "noinst": "<b>😥 Вы не ввели свой instagram</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "VK",
            "🚫 Link not set",
            lambda: "You VK LINK",
            "discord",
            "🚫 Link not set",
            lambda: "You discord LINK",
            "twitter",
            "🚫 Link not set",
            lambda: "You twitter LINK",
            "inst",
            "🚫 Link not set",
            lambda: "You instagram LINK",
            "grustno",
            "🚫 Link not set",
            lambda: "You grustnogram LINK",
            "telegram",
            "🚫 Link not set",
            lambda: "You telegram chanel LINK",
        )

    @loader.unrestricted
    async def vizitkacmd(self, message: Message) -> None:
        """Command for displaying a business card"""
        await utils.answer(message, self.strings("httpserr"))
        await asyncio.sleep(5)
        await message.delete()
        await self.inline.form(
            message=message,
            text=self.strings("mysocial"),
            reply_markup=[
                [
                    {"text": "🥱 Dicord", "url": self.config["discord"]},
                    {"text": "🦢 VK", "url": self.config["VK"]},
                ],
                [
                    {"text": "🔰 Instagram", "url": self.config["inst"]},
                    {"text": "🎉 Grustnogram", "url": self.config["grustno"]},
                ],
                [
                    {"text": "🌐 Twitter", "url": self.config["twitter"]},
                    {"text": "💫 TG Channel", "url": self.config["telegram"]},
                ],
            ],
        )
