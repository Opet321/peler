# code by @xtdevs
# library RyuzakiLib

# code by @xtdevs
# library RyuzakiLib
import os
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import *
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram import filters
from pyrogram.types import *

from naya import *
from naya.config import *
from . import *

from typing import Optional

def get_text(
    message: Message,
    save_link: Optional[bool] = None,
) -> Optional[str]:
    text_ = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text_ = (
            message.reply_to_message.text
            or message.reply_to_message.caption
            or message.reply_to_message.caption_entities
        )

    if text_ is None:
        return False
    else:
        if save_link:
            return str(text_)
        else:
            return str(text_.lower())

@bots.on_message(filters.command(["ai", "ask"], cmd) & filters.me)
async def chatgpt_support(client: Client, message: Message):
    pro = await message.edit_text("`Processing.....`")
    biji = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    biji = get_text(message)
    if not biji:
        await pro.edit_text("Berikan permintaan dari chatgpt")
        return
    try:
        hacking = RendyDevChat(biji).get_response.model(model_id=5, re_json=True, is_models=True, status_ok=True)
        await client.send_message(
            message.chat.id,
            hacking["randydev"].get("message"),
            reply_to_message_id=message.id
        )
        await pro.delete()
    except Exception as e:
        await pro.edit_text(str(e))

__MODULE__ = "chatgpt"
__HELP__ = f"""

Bantuan Untuk Chatgpt 

• perintah: <code>{cmd}ai</code> [query]
• penjelasan: Untuk mengajukan pertanyaan ke AI
"""
