"""

█▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
from ..inline.types import InlineCall

# meta developer: @shadow_modules, @hikarimods


@loader.tds
class NewsLetterMod(loader.Module):
    strings = {
        "name": "NewsLetter",
        "succnews": "<b>✅ Newsletter successfully sent</b>\n<b>👁‍🗨 Chats that were sent:</b>\n{}",
        "nochat": "<b>No chat to send</b>",
        "warnform": "<b>⚠️ Attention!</b>\n<b>😰 When sending a newsletter to a lot of chats, there may be a flood</b>\n<b>✅ If you agree that you can get a flood, click on the button below</b>",
        "noargs": "<b>😥 There are no messages to send</b>",
        "yes": "✅ Yes",
        "no": "❌ No",
    }
    strings_ru = {
        "succnews": "<b>✅ Рассылка успешно отправлена</b>\n<b>👁‍🗨 Чаты в которые была отправлена рассылка:</b>\n{}",
        "nochat": "<b>Нет чата для рассылки</b>",
        "warnform": "<b>⚠️ Внимание!</b>\n<b>😰 При отправке рассылки во многое количество чатов может быть флудвейт</b>\n<b>✅ Если вы согласны с тем что можете получить флудвейт - нажмите на кнопку ниже</b>",
        "noargs": "<b>😥 Нет сообщения что-бы рассылать</b>",
        "yes": "✅ Да",
        "no": "❌ Нет",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chats",
                [],
                lambda: "Chat for newsletter",
                validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("^@[a-zA-Z0-9_]{1,32}$"),
                    ),
                ),
            ),
        )

    async def sendnewscmd(self, message: Message):
        if self.get("warn") == "no":
            await self.inline.form(
                message=message,
                text=self.strings("warnform"),
                reply_markup=[
                    [
                        {
                            "text": self.strings("yes"),
                            "callback": self.inline__callAnswer,
                            "args": ("yes",),
                        },
                    ],
                    [
                        {
                            "text": self.strings("no"),
                            "callback": self.inline__callAnswer,
                            "args": ("no",),
                        },
                    ],
                ],
            )
            return

        args = utils.get_args_raw(message)
        chats = self.config["chats"]
        try:
            for chat in chats:
                await self.client.send_message(chat, args)

            await utils.answer(
                message,
                self.strings("succnews").format("\n".join(map(str, chats))),
            )
        except ValueError:
            await utils.answer(message, self.strings("noargs"))

    async def inline__callAnswer(self, call: InlineCall, value: str):
        self.set("warn", value)
        await call.delete()
