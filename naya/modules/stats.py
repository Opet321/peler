# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from datetime import datetime

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from . import *


@bots.on_message(filters.me & filters.command(["stats"], cmd))
async def stats(client: Client, message: Message):
    Man = await message.edit_text("`Mengambil info akun ...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Man.edit_text(
        """`Status akun anda, berhasil diambil dalam {} detik`
` {} Pesan Pribadi.`
`berada di {} Groups.`
`berada {} Super Groups.`
`berada {} Channels.`
`menjadi admin di {} Chats.`
`Bots = {}`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )


__MODULE__ = "stats"
__HELP__ = f"""
Bantuan Untuk Stats

• perintah: <code>{cmd}stats</code>
• penjelasan: Melihat informasi akun anda.
"""
