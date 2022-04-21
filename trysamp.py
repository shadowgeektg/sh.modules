"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
import random

# scope: meta developer: @shadow_geektg

@loader.tds
class TrySampMod(loader.Module):
    strings = {"name": "TrySamp"}

    async def trycmd(self, message: Message) -> None:
        rand = ["Удачно", "Не удачно", "Не удачно", "Удачно"]
        tryrandom = random.choice(rand)
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, f"<b>{tryrandom}</b>")
        else:
            await utils.answer(message, f"<b>{tryrandom} | {args}</b>")