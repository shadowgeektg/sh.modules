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
# meta developer: @shadow_hikka, @dan_endy, @hikariatama

logger = logging.getLogger(__name__)


@loader.tds
class InlineVizitkaMod(loader.Module):
    strings = {
        "name": "InlineVizitka",
        "mysocial": "<b>✨ My social networks</b>",
        "userules": "<b>How this module is used</b>\n1. Links to social networks must be entered in <code>{prefix}config</code>\n2. Links in the config must start with https:// otherwise there will be an <b>error</b>",
    }

    strings_ru = {
        "mysocial": "<b>✨ Мои соцсети</b>",
        "userules": "<b>Как пользоваться данным модулем</b>\n1. Ссылки на соц.сети надо вводить в <code>{prefix}config</code>\n2. Ссылки в конфиге должны начинаться с https:// иначе будет <b>ошибка</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "custom_message",
            "<b>✨ Мои соцсети</b>",
            lambda: "Custom message in .vizitka",
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
            "gitlab",
            "🚫 Link not set",
            lambda: "You gitlab account LINK",
            "github",
            "🚫 Link not set",
            lambda: "You github account LINK",
            "twitch",
            "🚫 Link not set",
            lambda: "You twitch LINK",
            "anixart",
            "🚫 Link not set",
            lambda: "You anixart LINK",
            "xda",
            "🚫 Link not set",
            lambda: "You xda LINK",
            "4pda",
            "🚫 Link not set",
            lambda: "You 4pda LINK",
            "tiktok",
            "🚫 Link not set",
            lambda: "You tiktok LINK",
            "pinterest",
            "🚫 Link not set",
            lambda: "You pinterest LINK",
            "spotify",
            "🚫 Link not set",
            lambda: "You spotify LINK",
            "pixiv",
            "🚫 Link not set",
            lambda: "You pixiv LINK",
        )

    @loader.unrestricted
    async def vizitkacmd(self, message: Message) -> None:
        """Command for displaying a business card"""
        await self.inline.form(
            message=message,
            text=self.config["custom_message"],
            reply_markup=[
                [
                    {"text": "🥱 Discord", "callback": self.inline__callAnswer},
                    {"text": "🦢 VK", "url": self.config["VK"]},
                ],
                [
                    {"text": "❤ Instagram", "url": self.config["inst"]},
                    {"text": "🖤 Grustnogram", "url": self.config["grustno"]},
                ],
                [
                    {"text": "🌐 Twitter", "url": self.config["twitter"]},
                    {"text": "💫 TG Channel", "url": self.config["telegram"]},
                ],
                [
                    {"text": "🌚 GitHub", "url": self.config["github"]},
                    {"text": "☀ GitLab", "url": self.config["gitlab"]},
                ],
                [
                    {"text": "😽 Anixart", "url": self.config["anixart"]},
                    {"text": "📱 4PDA", "url": self.config["4pda"]},
                ],
                [
                    {"text": "📺 Twitch", "url": self.config["twitch"]},
                    {"text": "📴 XDA", "url": self.config["xda"]},
                ],
                [
                    {"text": "🤣 Tik tok", "url": self.config["tiktok"]},
                    {"text": "🎧 Spotify", "url": self.config["spotify"]},
                ],
                [
                    {"text": "🖌 Pixiv", "url": self.config["pixiv"]},
                    {"text": "🖌 Pinterest", "url": self.config["pinterest"]},
                ],
            ],
        )

    async def inline__callAnswer(self, call) -> None:
        await call.answer(self.config["discord"], show_alert=True)

    async def vizinfocmd(self, message: Message) -> None:
        await utils.answer(
            message, self.strings("userules").format(prefix=self.get_prefix())
        )
