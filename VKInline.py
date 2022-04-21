"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
import re

# scope: hikka_only
# scope: meta developer: @shadow_hikka, @dan_endy

@loader.tds
class VKInlineMod(loader.Module):
    strings = {"name": "MyVKInline", "myvk": "<b>👾 My VK</b>", "clickvk": "🦢 Click", "novk": "<b>😰 You didn't enter your VK</b>", "httpserr": "<b>❌ Invalid link in config\n✔ The link must start with</b> <code>https://</code>"}

    strings_ru = {"myvk": "<b>👾 Мой VK</b>", "clickvk": "🦢 Нажми", "novk": "<b>😰 Вы не ввели свой вк</b>", "httpserr": "<b>❌ Недопустимая ссылка в конфиге\n✔ Ссылка должна начинаться на</b> <code>https://</code>"}

    def __init__(self):
        self.config = loader.ModuleConfig("VK","", lambda: "You VK")

    
    @loader.unrestricted
    async def myvkcmd(self, message: Message) -> None:
        """The command to display your VK"""
        if len(self.config["VK"]) == 0:
            await utils.answer(message, self.strings("novk", message))
            return
        elif "https://" in self.config["VK"]:
            await self.inline.form(
                text=self.strings("myvk"),
                message=message,
                disable_security=True,
                reply_markup=[
                    [
                        {
                            "text": self.strings("clickvk"),
                            "url": self.config["VK"]
                        }
                    ]
                ],
            )
        else:
            await utils.answer(message, self.strings("httpserr"))
            return
 
