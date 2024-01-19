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


COPY_ID = {}


async def download_media_copy(get, client, infomsg, message):
    msg = message.reply_to_message or message
    text = get.caption or ""
    if get.photo:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "Download Photo",
                get.photo.file_id,
            ),
        )
        await client.send_photo(
            message.chat.id,
            media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.animation:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "Download Animation",
                get.animation.file_id,
            ),
        )
        await client.send_animation(
            message.chat.id,
            animation=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.voice:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(infomsg, time(), "Download Voice", get.voice.file_id),
        )
        await client.send_voice(
            message.chat.id,
            voice=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.audio:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "Download Audio",
                get.audio.file_id,
            ),
        )
        thumbnail = await client.download_media(get.audio.thumbs[-1]) or None
        await client.send_audio(
            message.chat.id,
            audio=media,
            duration=get.audio.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)
        os.remove(thumbnail)

    elif get.document:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "Download Document",
                get.document.file_id,
            ),
        )
        await client.send_document(
            message.chat.id,
            document=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.video:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "Download Video",
                get.video.file_name,
            ),
        )
        thumbnail = await client.download_media(get.video.thumbs[-1]) or None
        await client.send_video(
            message.chat.id,
            video=media,
            duration=get.video.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)
        os.remove(thumbnail)


@bots.on_message(filters.command(["copy"], cmd) & filters.me)
async def _(client, message):
    msg = message.reply_to_message or message
    infomsg = await message.reply(" <b>Processing...</b>")
    link = get_arg(message)
    if not link:
        return await infomsg.edit("<b>{message.text}</b> [link]</b>")
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
                try:
                    text = f"get_colong {id(message)}"
                    x = await client.get_inline_bot_results(app.me.username, text)
                    results = await client.send_inline_bot_result(
                        message.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=msg.id,
                    )
                    COPY_ID[client.me.id] = int(results.updates[0].id)
                    await infomsg.delete()
                except Exception as error:
                    await infomsg.edit(f"{str(error)}")
    else:
        await infomsg.edit("Link yang anda masukkan tidak valid.")


@app.on_inline_query(filters.regex("^get_colong"))
async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Klik Disini",
                                    callback_data=f"colongmsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 Konten Yang Mau Diambil Bersifat Private✅</b>"
                    ),
                )
            )
        ],
    )


@app.on_callback_query(filters.regex("^colongmsg_"))
async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        await m._client.unblock_user(app.me.username)
        await callback_query.edit_message_text("<b>Processing...</b>")
        copy = await m._client.send_message(
            app.me.username, f"/copy {m.text.split()[1]}"
        )
        msg = m.reply_to_message or m
        await asyncio.sleep(1.5)
        await copy.delete()
        async for get in m._client.search_messages(app.me.username, limit=1):
            await m._client.copy_message(
                m.chat.id, app.me.username, get.id, reply_to_message_id=msg.id
            )
            await m._client.delete_messages(m.chat.id, COPY_ID[m._client.me.id])
            await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<b>{error}</b>")
