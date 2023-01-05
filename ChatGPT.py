# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyleft 2022 t.me/shadow_modules
# This module is free software
# You can edit this module

# meta developer: @shadow_modules
# meta banner: https://i.imgur.com/OM64rlU.jpeg


import openai
from .. import loader, utils
from telethon.tl.types import Message  # type: ignore
import random

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt


@loader.tds
class ChatGPTMod(loader.Module):
    strings = {
        "name": "ChatGPT",
        "wait": "<emoji document_id=5471981853445463256>🤖</emoji><b> ChatGPT generating response, please wait</b>",
        "quest": "\n\n\n<emoji document_id=5819167501912640906>❔</emoji><b> Your question to ChatGPT was:</b> {args}",
    }
    strings_ru = {
        "wait": "<emoji document_id=5471981853445463256>🤖</emoji><b> ChatGPT генерирует ответ, подождите</b>",
        "quest": "\n\n\n<emoji document_id=5819167501912640906>❔</emoji><b> Ваш вопрос к ChatGPT был:</b> {args}",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                lambda: "Api key for ChatGPT",
                validator=loader.validators.Hidden(),
            ),
        )

    async def gptcmd(self, message: Message):
        args = utils.get_args_raw(message)
        await utils.answer(message, self.strings("wait").format(args=args))
        openai.api_key = self.config["api_key"]
        model_engine = "text-davinci-003"
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=args,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        await utils.answer(message, response + self.strings("quest").format(args=args))
