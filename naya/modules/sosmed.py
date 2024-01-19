#memek
import asyncio

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory

from . import *

__MODULE__ = "sosmed"
__HELP__ = f"""
Bantuan Untuk sosmed

• perintah: <code>{cmd}tt</code> [link]
• penjelasan: Untuk mengunduh media dari Tiktok.

• perintah: <code>{cmd}twit</code> [link]
• penjelasan: Untuk mengunduh media dari Twitter.

• perintah: <code>{cmd}sd</code> [link]
• penjelasan: Untuk mengunduh media dari ig, tt, pint.
"""

@bots.on_message(filters.me & filters.command("tt", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "downloader_tiktok_bot"
    await client.unblock_user(bot)
    await client.send_message(bot, link)
    # await xnxx.delete()
    await asyncio.sleep(8)
    async for sosmed in client.search_messages(bot):
        try:
            if sosmed.video:
                await sosmed.copy(
                    message.chat.id,
                    caption=f"<b>upload by {app.me.mention} </b>",
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
            else:
                try:
                    if sosmed.photo:
                        await sosmed.copy(
                            message.chat.id,
                            caption=f"<b>upload by {app.me.mention} </b>",
                            reply_to_message_id=message.id,
                        )
                        await Tm.delete()
                except Exception:
                    await Tm.edit(
                        "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
                    )
        except Exception:
            pass
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))



@bots.on_message(filters.me & filters.command("twit", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "twitter_video_downloader_bot"
    await client.unblock_user(bot)
    await client.send_message(bot, link)
    # await xnxx.delete()
    await asyncio.sleep(8)
    async for sosmed in client.search_messages(bot):
        try:
            if sosmed.video:
                await sosmed.copy(
                    message.chat.id,
                    caption=f"<b>upload by {app.me.mention} </b>",
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
            else:
                try:
                    if sosmed.photo:
                        await sosmed.copy(
                            message.chat.id,
                            caption=f"<b>upload by {app.me.mention} </b>",
                            reply_to_message_id=message.id,
                        )
                        await Tm.delete()
                except Exception:
                    await Tm.edit(
                        "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
                    )
        except Exception:
            pass
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@bots.on_message(filters.me & filters.command("sd", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "SaveAsbot"
    await client.unblock_user(bot)
    await client.send_message(bot, link)
    # await xnxx.delete()
    await asyncio.sleep(8)
    async for sosmed in client.search_messages(bot):
        try:
            if sosmed.video:
                await sosmed.copy(
                    message.chat.id,
                    caption=f"",
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
            else:
                try:
                    if sosmed.photo:
                        await sosmed.copy(
                            message.chat.id,
                            caption=f"",
                            reply_to_message_id=message.id,
                        )
                        await Tm.delete()
                except Exception:
                    await Tm.edit(
                        "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
                    )
        except Exception:
            pass
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
