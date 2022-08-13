# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

from .. import loader, utils
from telethon.tl.types import Message

# meta developer: @shadow_geektg, @dan_endy
# scope: hikka_only


@loader.tds
class VKInlineMod(loader.Module):
    strings = {
        "name": "MyVKInline",
        "myvk": "<b>👾 My VK</b>",
        "clickvk": "🦢 Click",
        "novk": "<b>😰 You didn't enter your VK</b>",
    }

    strings_ru = {
        "myvk": "<b>👾 Мой VK</b>",
        "clickvk": "🦢 Нажми",
        "novk": "<b>😰 Вы не ввели свой вк</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "VK",
                None,
                lambda: "Your VK",
                validator=loader.validators.Link(),
            )
        )

    @loader.unrestricted
    async def myvkcmd(self, message: Message):
        """The command to display your VK"""
        if not self.config["VK"]:
            await utils.answer(message, self.strings("novk", message))
            return
        elif "https://" in self.config["VK"]:
            await self.inline.form(
                text=self.strings("myvk"),
                message=message,
                reply_markup={"text": self.strings("clickvk"), "url": self.config["VK"]},
            )
