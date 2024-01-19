import os
import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram import filters
from pyrogram.types import *

from . import *

__MODULE__ = "nyolong"
__HELP__ = f"""
Bantuan Untuk Nyolong

• perintah: <code>{cmd}copy</code> [link]
• penjelasan: Untuk mengambil konten ch private.

• perintah: <code>{cmd}nyolong</code> [link]
• penjelasan: Untuk mengambil konten ch private.
"""



@bots.on_message(filters.me & filters.command("copy", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "Nyolong_lagi_bot"
    await client.unblock_user(bot)
    xnxx = await client.send_message(bot, link)
    await xnxx.delete()
    await asyncio.sleep(1)
    await Tm.delete()
    async for sosmed in client.search_messages(bot, limit=1):
        try:
            await sosmed.copy(
                message.chat.id,
                reply_to_message_id=message.id,
            )
        except Exception:
            await Tm.edit(
                "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
            )
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@bots.on_message(filters.command(["nyolong"], cmd) & filters.me)
async def nyolongnih(client, message):
    await message.edit("Processing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Sepertinya terjadi kesalahan")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Sepertinya terjadi kesalahan")
    anjing = dia.caption or None
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Sepertinya terjadi kesalahan")
