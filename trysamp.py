# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# meta banner: https://i.imgur.com/OM64rlU.jpeg

from .. import loader, utils
from telethon.tl.types import Message  
import random


@loader.tds
class TrySampMod(loader.Module):
    strings = {"name": "TrySamp"}

    async def trycmd(self, message: Message):
        tryrandom = random.choice(["Удачно", "Не удачно", "Не удачно", "Удачно"])
        args = utils.get_args_raw(message)
        await utils.answer(
            message, f"<b>{tryrandom} | {args}</b>" if args else f"<b>{tryrandom}</b>"
        )
