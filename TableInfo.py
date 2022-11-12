# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/OM64rlU.jpeg

from .. import loader, utils

import logging

from telethon.tl.functions.channels import CreateChannelRequest  # type: ignore
from telethon.tl.types import Message  # type: ignore

logger = logging.getLogger(__name__)


class TableMod(loader.Module):
    """Информация о знакомых"""

    strings = {
        "name": "TableMod",
        "no_args": "<b>😥 Arguments not found</b>",
        "args_incorrect": "<b>😰 Arguments are not correct\n✔ Example arguments: </b><code>.tableadd name|age|day|year|hobby|userid|geo</code>",
        "success": "<b>😊 Successfully added</b>",
        "dont_touch": "💾 Do not touch this chat\n😊It was created for the TableInfo module to work",
    }

    strings_ru = {
        "no_args": "<b>😥 Аргументы не найдены</b>",
        "args_incorrect": "<b>😰 Аргументы не правильные\n✔ Пример аргументов: </b><code>.tableadd name|age|day|year|hobby|userid|geo</code>",
        "success": "😊 Информация успешно добавлена",
        "dont_touch": "💾 Не трогайте этот чат\n😊Он был создан для работы модуля TableInfo",
    }

    async def getchat(self, reset: bool = False) -> int:
        chat_id = self.get("chat_id")
        if not reset:
            if chat_id:
                return chat_id
            chat_id = [
                chat
                for chat in await self.client.get_dialogs()
                if chat.name == "TableInfo"
            ]
            if chat_id:
                return chat_id[0].id
        chat_id = (
            (
                await self.client(
                    CreateChannelRequest(
                        title="TableInfo",
                        about=self.strings("dont_touch"),
                        megagroup=True,
                    )
                )
            )
            .chats[0]
            .id
        )
        await utils.set_avatar(
            client=self.client,
            peer=chat_id,
            avatar="https://i.pinimg.com/736x/08/16/de/0816de86e13fa2b099c2546aa9c4a205.jpg",
        )
        self.set("chat_id", chat_id)
        return chat_id

    async def tableaddcmd(self, message: Message):
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_args"))
            return

        args = args.split("|")

        if len(args) != 7:
            await utils.answer(message, self.strings("args_incorrect"))
            return

        name, age, day, year, hobby, userid, geo = args
        chat = await self.getchat()
        text = (
            f"👨‍🦰 <b>Имя:</b> <i>{name}</i>\n"
            f"📟 <b>Возраст:</b> <i>{age}</i>\n"
            f"🎂 <b>День рождения:</b> <i>{day}</i>\n"
            f"📅 <b>Год рождения:</b> <i>{year}</i>\n"
            f"🎭 <b>Хобби:</b> <i>{hobby}</i>\n"
            f"🖥 <b>Айди пользователя:</b> <a href='tg://user?id={userid}'>{userid}</a>\n"
            f"📍 <b>Местоположение:</b> <i>{geo}</i>\n"
        )

        try:
            await self.client.send_message(chat, text)
        except Exception as e:
            logger.debug(f"Error while sending message to chat: {e}")
            chat = await self.getchat(True)
            await self.client.send_message(chat, text)

        await utils.answer(message, self.strings("success"))
