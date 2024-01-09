# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyright 2023 t.me/shadow_modules
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# meta developer: @shadow_modules
# meta banner: https://i.imgur.com/aGGx93G.jpeg

from .. import loader, utils
from telethon.tl.types import Message  # type: ignore
from telethon.tl.functions.channels import CreateChannelRequest  # type: ignore
from telethon.tl.functions.channels import UpdateUsernameRequest  # type: ignore
import logging


@loader.tds
class CheckerUsernamesMod(loader.Module):
    """Check of avaliable usernames"""

    strings = {
        "name": "CheckerUsernames",
        "off": "<emoji document_id=5350311258220404874>❗️</emoji> <b>Checker disabled</b>",
        "on": "<emoji document_id=5776375003280838798>✅</emoji> <b>Checker enabled</b>",
    }
    strings_ru = {
        "off": "<emoji document_id=5350311258220404874>❗️</emoji> <b>Проверка юзернеймов выключена</b>",
        "on": "<emoji document_id=5776375003280838798>✅</emoji> <b>Проверка юзернеймов включена</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "usernames",
                ["onetimeusername"],
                lambda: "Usernames for check",
                validator=loader.validators.Series(
                    validator=loader.validators.String()
                ),
            ),
            loader.ConfigValue(
                "text",
                "OCCUPIED BY SH. MODULE",
                lambda: "Usernames for check",
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "delay",
                5,
                lambda: "Delay for check username",
                validator=loader.validators.Integer(minimum=0),
            ),
        )

    @loader.loop(30, autostart=True)
    async def checker(self):
        if not self.get("status"):
            return
        usernames = self.config["usernames"]
        for username in usernames:
            try:
                await self.client.get_entity(username)
            except ValueError:
                logging.warning(f"{username} is incorrect")
                chan = await self.client(
                    CreateChannelRequest(
                        title="occupied shadow",
                        about="GEAR SHADOW",
                    )
                )
                await self.client(UpdateUsernameRequest(chan.chats[0].id, username))
                await self.client.send_message(chan.chats[0].id, self.config["text"])
                continue

    async def cusercmd(self, message: Message):
        if self.get("status"):
            await utils.answer(message, self.strings("off"))
            return self.set("status", False)
        else:
            await utils.answer(message, self.strings("on"))
            self.set("status", True)
