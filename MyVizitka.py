"""
    █▀ █ █ ▄▀█ █▀▄ █▀█ █ █ █
    ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

    Copyleft 2022 t.me/shadow_modules
    This module is free software
    You can edit this module
"""

from .. import loader, utils
from telethon.tl.types import Message
import logging
from telethon.utils import get_display_name

# scope: hikka_only
# meta developer: @shadow_hikka

logger = logging.getLogger(__name__)


@loader.tds
class MyVizitkaMod(loader.Module):
    strings = {"name": "MyVizitka"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_message",
                "<b>Тест</b>",
                lambda: "Custom message in .myvizit\nMay contain {me}, {prefix}, {platform} keywords",
            ),
            loader.ConfigValue(
                "button_1",
                ["My chat", "https://t.me/shadowmodschat"],
                lambda: "You 1 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button_2",
                ["My channel", "https://t.me/shadow_modules"],
                lambda: "You 2 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button_3",
                ["My account", "https://t.me/shadow_hikka"],
                lambda: "You 3 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button_4",
                [],
                lambda: "You 4 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button_5",
                [],
                lambda: "You 5 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button_6",
                [],
                lambda: "You 6 button",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "file_url",
                "https://i.pinimg.com/564x/b9/30/e6/b930e6476d705d7e92f7b961e61d5141.jpg",
                lambda: "Direct link to photo/video/gif/music",
            ),
            loader.ConfigValue(
                "type_file",
                "photo",
                lambda: "Type of file specified in file_url",
                validator=loader.validators.Choice(["photo", "video", "audio", "gif"]),
            ),
        )

    def _get_mark(self, btn_count):
        btn_count = str(btn_count)
        return (
            {
                "text": self.config[f"button_{btn_count}"][0],
                "url": self.config[f"button_{btn_count}"][1],
            }
            if self.config[f"button_{btn_count}"]
            else None
        )

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.me = await client.get_me()

    @loader.unrestricted
    async def myvizitcmd(self, message: Message) -> None:
        """Command for displaying a business card"""
        me = f'<b><a href="tg://user?id={self.me.id}">{get_display_name(self.me)}</a></b>'
        prefix = self.get_prefix()
        platform = utils.get_named_platform()
        await self.inline.form(
            disable_security=True,
            message=message,
            text=self.config["custom_message"].format(
                me=me, prefix=prefix, platform=platform
            ),
            reply_markup=[
                [
                    *([m[1]] if m[1] else []),
                    *([m[2]] if m[2] else []),
                    *([m[3]] if m[3] else []),
                ],
                [
                    *([m[4]] if m[4] else []),
                    *([m[5]] if m[5] else []),
                    *([m[6]] if m[6] else []),
                ],
            ],
            **{self.config["type_file"]: self.config["file_url"]},
        )

    async def myvizit_inline_handler(self, query: "InlineQuery") -> str:
        """Inline myvizit"""
        m = {x: self._get_mark(x) for x in range(7)}
        me = f'<b><a href="tg://user?id={self.me.id}">{get_display_name(self.me)}</a></b>'
        prefix = self.get_prefix()
        platform = utils.get_named_platform()

        return {
            "title": "MyVizitka",
            "description": "My business card",
            "message": self.config["custom_message"].format(
                me=me, prefix=prefix, platform=platform
            ),
            "thumb": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Info_Simple_bw.svg/1200px-Info_Simple_bw.svg.png",
            "reply_markup": [
                [
                    *([m[1]] if m[1] else []),
                    *([m[2]] if m[2] else []),
                    *([m[3]] if m[3] else []),
                ],
                [
                    *([m[4]] if m[4] else []),
                    *([m[5]] if m[5] else []),
                    *([m[6]] if m[6] else []),
                ],
            ],
        }
