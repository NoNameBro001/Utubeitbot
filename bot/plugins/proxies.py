import asyncio
import os
import requests

from ..config import Config
from ..utubebot import UtubeBot
from ..translations import Messages as tr
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from ..helpers.database import db



@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("proxies")
)
async def proxies(c: UtubeBot, m: Message):
    username = "1owsgh8w5iux12r"
    password = "3atwlzo7997woep"
    proxy = "rp.proxyscrape.com:6060"
    proxy_auth = "{}:{}@{}".format(username, password, proxy)
    proxies = {
            "http":"http://{}".format(proxy_auth),
            "https":"https://{}".format(proxy_auth)
    }
    urlToGet = "http://ip-api.com/json"
    r = requests.get(urlToGet , proxies=proxies)
    print("Response:\n{}".format(r.text))
    await m.reply_text(
        text="Proxies:\n{}".format(r.text),
        quote=True
    )
