import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/ed6c1032e70b8a444c29f.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**♡ I'ᴍ sᴡᴀʟʟᴏWᴛᴀɪʟ ʀᴏʙᴏᴛ** \n\n"
    TEXT += f"**♡ I'm Working ᴘʀᴏᴘᴇʀʟʏ** \n\n"
    TEXT += f"**♡ sᴇᴄʀᴇ: LATEST Version** \n\n"
    TEXT += f"**♡ My Creator: [ naruto](http://t.me/lord_seventh_hokage_naruto)** \n\n"
    TEXT += f"**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @nero_x_support** \n\n"
    TEXT += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ **"
    BUTTON = [
        [
            Button.url(" Updates", "https://t.me/nero_x_updates"),
            Button.url(" Support", "https://t.me/nero_x_support"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
