# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import asyncio
import os

from . import *

from pyrogram.raw.functions.messages import DeleteHistory

@bots.on_message(filters.me & filters.command(["q"], cmd))
async def quotly_cmd(client, message):
    info = await eor(message, "`processing.....`")
    await client.unblock_user("@QuotLyBot")
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except Exception as error:
                await info.edit(error)
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        try:
            for x in msg:
                await x.forward("@QuotLyBot")
        except Exception:
            pass
        await asyncio.sleep(9)
        await info.delete()
        async for quotly in client.get_chat_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                await message.reply(
                    f"❌ @QuotLyBot ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ ᴘᴇʀᴍɪɴᴛᴀᴀɴ", quote=True
                )
            else:
                sticker = await client.download_media(quotly)
                await message.reply_sticker(sticker, quote=True)
                os.remove(sticker)
    else:
        if len(message.command) < 2:
            return await info.edit("<b>ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ</b>")
        else:
            msg = await client.send_message(
                "@QuotLyBot", f"/qcolor {message.command[1]}"
            )
            await asyncio.sleep(1)
            get = await client.get_messages("@QuotLyBot", msg.id + 1)
            await info.edit(
                f"<b>ᴡᴀʀɴᴀ ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ᴋᴜᴛɪᴘᴀɴ ᴅɪsᴇᴛᴇʟ ᴋᴇ:</b> <code>{get.text.split(':')[1]}</code>"
            )
    user_info = await client.resolve_peer("@QuotLyBot")
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    
@bots.on_message(filters.me & filters.command("twitt"))
async def twitt(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Please Reply to Message**")
    bot = "TwitterStatusBot"
    if message.reply_to_message:
        await message.edit("`Making a post...`")
        await client.unblock_user(bot)
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for twitt in client.search_messages(bot, limit=1):
            if twitt:
                await message.delete()
                await message.reply_sticker(
                    sticker=twitt.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create twitter status**")
    try:          
        await client.delete_messages(bot, 2)
    except Exception:
        pass
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


__MODULE__ = "quote"
__HELP__ = f"""
Bantuan Untuk Quote

• perintah: <code>{cmd}twitt</code> [balas pesan]
• penjelasan: Untuk status Twitter.

• perintah: <code>{cmd}q</code> [balas pesan]
• penjelasan: Untuk quote.

• perintah: <code>{cmd}q</code> [balas pesan][angka]
• penjelasan: Ini akan membuat beberapan pesan menjadi quote.
"""
