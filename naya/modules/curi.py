import os
import asyncio

from pyrogram import *
from gc import get_objects
from time import time

from pyrogram import *
from pyrogram.types import *

from naya import *
from naya.utils import *
from pyrogram import filters
from pyrogram.types import *

from . import *

__MODULE__ = "curi"

__HELP__ = f"""
Bantuan Untuk Curi

• perintah: <code>{cmd}curi</code> [balas ke pesan]
• penjelasan: Untuk mengambil pap timer, cek pesan tersimpan.
"""


@bots.on_message(filters.command(["curi", "love"], cmd) & filters.me)
async def pencuri(client, message):
    dia = message.reply_to_message
    user_id = client.me.id
    me = await get_botlog(user_id)
    if not dia:
        await client.send_message(me, "`Mohon balas ke media.`")
    anjing = dia.caption or None
    mmk = await message.edit("`Processing...`")
    await mmk.delete()
    if dia.text:
        await dia.copy(me)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(me, anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(me, anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(me, anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(me, anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(me, anu, anjing)
        await message.delete()
        os.remove(anu)
    try:
        await client.send_message(me, "**Pap timernya tuh.**")
    except Exception as e:
        print(e)

@bots.on_message(filters.command(["copy"], cmd))
async def copy_bot_msg(client, message):
    if message.from_user.id not in ubot._bots:
        return

    Tm = await message.reply("ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ")
    link = get_arg(message)

    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )

    msg_id, chat = (int(link.split("/")[-1]), str(link.split("/")[-2]))

    try:
        get = await client.get_messages(chat, msg_id)
        await get.copy(message.chat.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(str(error))


async def download_media_copy(get, client, infomsg, message):
    msg = message.reply_to_message or message
    text = get.caption or ""

    media_types = ["photo", "animation", "voice", "audio", "document", "video"]
    for media_type in media_types:
        if hasattr(get, media_type):
            media_info = getattr(get, media_type)
            if media_info and hasattr(media_info, "file_id"):
                media = await client.download_media(
                    get,
                    progress=progress,
                    progress_args=(
                        infomsg,
                        time(),
                        Fonts.smallcap(f"download {media_type}"),
                        media_info.file_id,
                    ),
                )
                thumbnail = None

                if hasattr(media_info, "thumbs") and media_info.thumbs:
                    thumbnail = await client.download_media(media_info.thumbs[-1])

                if media:
                    send_function = getattr(client, f"send_{media_type}")
                    send_args = {
                        media_type: media,
                        "caption": text,
                        "reply_to_message_id": msg.id,
                    }

                    if media_type in ["audio", "video"] and hasattr(
                        media_info, "duration"
                    ):
                        send_args["duration"] = media_info.duration

                    if media_type in ["audio", "video"] and thumbnail:
                        send_args["thumb"] = thumbnail

                    await send_function(message.chat.id, **send_args)
                    await infomsg.delete()
                    os.remove(media)
                    if thumbnail:
                        os.remove(thumbnail)

@bots.on_message(filters.command(["copy"], cmd))
async def copy_ubot_msg(client, message):
    msg = message.reply_to_message or message
    infomsg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴏᴘʏ ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ</b>")
    link = get_arg(message)

    if not link:
        return await infomsg.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )

    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])

        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))

            try:
                get = await client.get_messages(chat, msg_id)
                try:
                    await get.copy(message.chat.id, reply_to_message_id=msg.id)
                    await infomsg.delete()
                except Exception:
                    await download_media_copy(get, client, infomsg, message)
            except Exception as e:
                await infomsg.edit(str(e))
        else:
            chat = str(link.split("/")[-2])

            try:
                get = await client.get_messages(chat, msg_id)
                await get.copy(message.chat.id, reply_to_message_id=msg.id)
                await infomsg.delete()
            except Exception:
                copy = await client.send_message(bot.me.username, f"/copy {link}")

                await asyncio.sleep(1.5)
                await copy.delete()

                async for get in client.search_messages(bot.me.username, limit=1):
                    await infomsg.delete()
                    await client.copy_message(
                        message.chat.id,
                        bot.me.username,
                        get.id,
                        reply_to_message_id=msg.id,
                    )
                    return await get.delete()
    else:
        return await infomsg.edit("ʟɪɴᴋ ʏᴀɴɢ ᴅɪ ᴍᴀsᴜᴋᴀɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")

@bots.on_message(filters.command(["wow"], cmd) & filters.me)
async def copy_ubot(client, message): 
     if len(message.command) >= 2: 
         return 
     reply = message.reply_to_message 
     if reply: 
         if reply.photo or reply.video: 
             await message.delete() 
             mtype = "photo" if reply.photo else "video" 
             media = await client.download_media(reply) 
             await getattr( 
                 client,  
                 f"send_{mtype}")( 
                     "me",  
                     media,  
                     reply.caption 
                 ) 
             os.remove(media)
 
            

   