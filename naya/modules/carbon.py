# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from io import BytesIO

from pyrogram import filters

from . import *


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@bots.on_message(filters.me & filters.command(["carbon"], cmd))
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.edit_text("`Berikan saya teks...`")
    ex = await message.edit_text("`Processing . . .`")
    carbon = await make_carbon(text)
    await ex.edit("`Uploading . . .`")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()


__MODULE__ = "carbon"
__HELP__ = f"""
Bantuan Untuk Carbon

• perintah: <code>{cmd}carbon</code> [balas pesan]
• penjelasan: Untuk membuat teks menjadi carbonara.
"""
