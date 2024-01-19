import asyncio

from pyrogram import *
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait
from pyrogram.types import *


from . import *

__MODULE__ = "broadcast"
__HELP__ = f"""
Bantuan Untuk Broadcast

• perintah: <code>{cmd}gucast</code> [text/reply to text/media]
• penjelasan: Untuk mengirim pesan ke semua user 
           
• perintah: <code>{cmd}gcast</code> [text/reply to text/media]
• penjelasan: Untuk mengirim pesan ke semua group 
           
• perintah: <code>{cmd}addbl</code>
• penjelasan: Menambahkan grup kedalam anti Gcast.
           
• perintah: <code>{cmd}delbl</code>
• penjelasan: Menghapus grup dari daftar anti Gcast.
           
• perintah: <code>{cmd}listbl</code>
• penjelasan: Melihat daftar grup anti Gcast.
           
"""

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg


async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats


@bots.on_message(filters.user(DEVS) & filters.command("cgcast", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command(["gcast"], cmd))
async def broadcast_group_cmd(client, message):
    msg = await eor(message, "`Processing . . .`")

    send = get_message(message)
    if not send:
        return await msg.edit("`Mohon bales sesuatu atau ketik sesuatu. . .`")

    chats = await get_broadcast_id(client, "group")
    blacklist = await blacklisted_chats(client.me.id)

    done = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        elif chat_id in BL_GCAST:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    await msg.edit(f"☑️ Pesan broadcast terkirim ke {done} group")
    await asyncio.sleep(5)
    await msg.delete()


@bots.on_message(filters.user(DEVS) & filters.command("cgucast", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command(["gucast"], cmd))
async def _(client, message: Message):
    sent = 0
    failed = 0
    msg = await message.reply("<code>Processing global broadcast...</code>")
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            elif len(message.command) < 2:
                return await msg.edit("Mohon berikan pesan atau balas ke pesan...")
            else:
                send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in DEVS:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(1)
                except Exception:
                    failed += 1
                    await asyncio.sleep(1)
    await msg.edit(f"**❏ Berhasil Terkirim: `{sent}` \n╰ Gagal Terkirim: `{failed}`**")
           
@bots.on_message(filters.me & filters.command(["addbl"], cmd))
async def bl_chat(client, message):
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)
    if chat.type == "private":
        return await message.reply("Maaf, perintah ini hanya berlaku untuk grup.")
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    bajingan = await blacklisted_chats(user_id)
    if chat in bajingan:
        return await message.reply("Obrolan sudah masuk daftar Blacklist Gcast.")
    await blacklist_chat(user_id, chat_id)
    await eor(
        message, "Obrolan telah berhasil dimasukkan ke dalam daftar Blacklist Gcast."
    )

@bots.on_message(filters.me & filters.command(["delbl"], cmd))
async def del_bl(client, message):
    if len(message.command) != 2:
        return await eor(
            message, "<b>Gunakan Format:</b>\n <code>delbl [CHAT_ID]</code>"
        )
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats(user_id):
        return await eor(
            message, "Obrolan berhasil dihapus dari daftar Blacklist Gcast."
        )
    whitelisted = await whitelist_chat(user_id, chat_id)
    if whitelisted:
        return await eor(
            message, "Obrolan berhasil dihapus dari daftar Blacklist Gcast."
        )
    await message.reply("Sesuatu yang salah terjadi.")


@bots.on_message(filters.me & filters.command(["listbl"], cmd))
async def all_chats(client, message):
    text = "<b>Daftar Blacklist Gcast:</b>\n\n"
    j = 0
    user_id = client.me.id
    chat_id = message.chat.id
    for count, chat_id in enumerate(await blacklisted_chats(user_id), 1):
        try:
            chat = await client.get_chat(chat_id)
            title = chat.title
        except Exception:
            title = "Private\n"
        j = 1
        text += f"<b>{count}.{title}</b><code{chat_id}</code>\n"
    if j == 0:
        await message.edit_text("Tidak Ada Daftar Blacklist Gcast.")
    else:
        await message.edit_text(text)
