# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/OM64rlU.jpeg

# Module author: @ftgmodulesbyfl1yd, @dekftgmodules, @memeframe
from .. import loader, utils


@loader.tds
class ChatMod(loader.Module):
    """Чат модуль"""

    strings = {"name": "Chat Tools"}

    async def echocmd(self, message):
        """Активировать/деактивировать Echo."""
        echos = self.db.get("Echo", "chats", [])
        chatid = str(message.chat_id)

        if chatid not in echos:
            echos.append(chatid)
            self.db.set("Echo", "chats", echos)
            return await message.edit("<b>[Echo Mode]</b> Активирован в этом чате!")

        echos.remove(chatid)
        self.db.set("Echo", "chats", echos)
        return await message.edit("<b>[Echo Mode]</b> Деактивирован в этом чате!")

    async def watcher(self, message):
        echos = self.db.get("Echo", "chats", [])
        chatid = str(message.chat_id)

        if chatid not in str(echos):
            return
        if message.sender_id == (await message.client.get_me()).id:
            return

        await message.client.send_message(
            int(chatid), message, reply_to=await message.get_reply_message() or message
        )
