# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import enums, filters

from . import *


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@bots.on_message(filters.command("setlog", cmd) & filters.me)
async def set_log(client, message):
    botlog_chat_id = message.chat.id
    user_id = client.me.id
    chat = await client.get_chat(botlog_chat_id)
    if chat.type == "private":
        return await message.reply("Maaf, perintah ini hanya berlaku untuk grup.")
    await set_botlog(user_id, botlog_chat_id)
    await message.reply_text(
        f"**ID Grup Log telah diatur ke `{botlog_chat_id}` untuk grup ini.**"
    )


__MODULE__ = "botlog"
__HELP__ = f"""
Bantuan Untuk Botlog

• perintah: <code>{cmd}setlog</code>
• penjelasan: Untuk mengaktifkan PMLogger dan TagLogger
"""
