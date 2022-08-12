# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# scope: hikka_only

from .. import loader, utils

import requests
import random

from telethon.tl.types import Message


async def photofox() -> str:
    """Fox photo handler"""
    return (await utils.run_sync(requests.get, "https://randomfox.ca/floof")).json()[
        "image"
    ]


async def photodog() -> str:
    """Dog photo handler"""
    return (await utils.run_sync(requests.get, "https://random.dog/woof.json")).json()[
        "url"
    ]


async def randomapi():
    randomapis = random.choice(
        ["https://randomfox.ca/floof", "https://random.dog/woof.json"]
    )
    if randomapis == "https://randomfox.ca/floof":
        return (
            await utils.run_sync(requests.get, "https://randomfox.ca/floof")
        ).json()["image"]
    elif randomapis == "https://random.dog/woof.json":
        return (
            await utils.run_sync(requests.get, "https://random.dog/woof.json")
        ).json()["url"]


@loader.tds
class FoxGalerryMod(loader.Module):
    """🦊 Foxes, Dogs 🐶"""

    strings = {"name": "FoxGallery"}

    strings_ru = {
        "_cls_doc": "🦊 Лисички, Песики 🐶",
        "_cmd_doc_foxes": "🦊 Лисички",
        "_cmd_doc_dogs": "🐶 Песики",
        "_cmd_doc_random": "🦊 Лисички и Песики 🐶",
    }

    async def foxescmd(self, message: Message):
        """🦊 Sending photos with foxes"""
        await self.inline.gallery(message, photofox)

    async def dogscmd(self, message: Message):
        """🐶 Sending photos with dogs"""
        await self.inline.gallery(message, photodog)

    async def randomcdfcmd(self, message: Message):
        """Photos of dogs 🐶 and foxes 🦊"""
        await self.inline.gallery(message, randomapi)
