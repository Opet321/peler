# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
import datetime
import re
import sys
from datetime import datetime
from os import environ, getpid, execle

import dotenv
import psutil
import urllib3

HAPP = None
import urllib3 
from time import time
from naya.utils import *
from naya.utils.db import *
from naya.load import CMD_HELP
from pyrogram.raw.functions import Ping
from pyrogram.types import *

from naya.config import *

from . import *
from .ping import START_TIME, _human_time_duration

from . import (
    StartTime,
    time_formatter,)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

photo = "naya/resources/logo.jpg"

@app.on_callback_query(
    filters.regex("sys_stats")
)
async def _sys_callback(
    client,
    cq: CallbackQuery,
):
    text = sys_stats()
    await app.answer_callback_query(
        cq.id,
        text,
        show_alert=True,
    )

def sys_stats():
    cpu = psutil.cpu_percent()
    mem = (
        psutil.virtual_memory().percent
    )
    disk = psutil.disk_usage(
        "/"
    ).percent
    process = psutil.Process(getpid())
    stats = f"""
PYROBOT-Premium
-----------------------
UPTIME: {time_formatter((time.time() - StartTime) * 1000)}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
-----------------------

Copyright (C) 2023-present fvnky

"""
    return stats

@bots.on_message(filters.command(["help"], cmd) & filters.me)
async def help_cmd(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(app.me.username, "help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(error)
    else:
        module = get_arg(message)
        if module in CMD_HELP:
            await message.reply(
                CMD_HELP[module].HELP + "\n<b> ©mengontol </b>",
                quote=True,
            )
        else:
            await message.reply(
                f"<b>❌ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴍᴏᴅᴜʟᴇ ᴅᴇɴɢᴀɴ ɴᴀᴍᴀ <code>{module}</code></b>"
            )


@bots.on_message(filters.command(["alive"], cmd) & filters.me)
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            app.me.username, f"user_alive_command {message.id} {message.from_user.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await message.reply(error)


@app.on_inline_query(filters.regex("^user_alive_command"))
async def _(client, inline_query):
    inline_query.query.split()    
    status1 = "Official"
    for bot in botlist:
        users = 0
        group = 0
        async for dialog in bot.get_dialogs():
            if dialog.chat.type == enums.ChatType.PRIVATE:
                users += 1
            elif dialog.chat.type in (
                enums.ChatType.GROUP,
                enums.ChatType.SUPERGROUP,
            ):
                group += 1
        if bot.me.id in DEVS:
            status = "Official"
        elif bot.me.id == OWNER:
            status = "Official"        
        else:
            status = "admin"
        antipm = None
        cekpc = await get_var(bot.me.id, "ENABLE_PM_GUARD")
        if not cekpc:
            antipm = "disable"
        else:
            antipm = "enable"
        nyugs = inline_query.from_user.id
        start = datetime.now()
        await bot.invoke(Ping(ping_id=0))
        ping = (datetime.now() - start).microseconds / 1000
        uptime_sec = (datetime.utcnow() - START_TIME).total_seconds()
        uptime = await _human_time_duration(int(uptime_sec))
        kontols = await check_antipm(nyugs)
        try:
            kurukuru = kontols["antipm"]
        except:
            kurukuru = "False"
        msg = f"""
<b>Security patch</b>
     <b>status:</b> [{status}]
        <b>Super Group:</b> <code>{group}</code>
        <b>Super User:</b> <code>{users}</code>
        <b>Anti Virus:</b> <code>{antipm}</code>
        <b>Clean Master:</b> <code>{kurukuru}</code>
        <b>Ubot ping:</b> <code>{ping}</code>
        <b>Ubot uptime:</b> <code>{uptime}</code>
"""
        await client.answer_inline_query(
            inline_query.id,
            cache_time=300,
            results=[
                InlineQueryResultArticle(
                    title="💬",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ᴄʟᴏsᴇ", callback_data="alv_cls"    
                                ),
                                InlineKeyboardButton(
                                    text="sᴛᴀᴛs", callback_data="sys_stats"
                                 
                                ),
                            ]
                        ]
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            ],
        )




@app.on_inline_query(filters.regex("^help"))
async def _(client, inline_query):
    msg = f"""
    <b>Help Modules<b>
     <b>Prefixes:</b> <code>{cmd}</code></b>
     <b>Commands: {len(CMD_HELP)}</b>
    """
    await client.answer_inline_query(
        inline_query.id,
        cache_time=300,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Module",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, CMD_HELP, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def _(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    if mod_match:
        module = mod_match[1].replace(" ", "_")
        text = f"<b>{CMD_HELP[module].__HELP__}</b>\n"
        button = [[InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ •", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text + "<b> ©mengontol </b>",
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    prev_text = f"""
    <b>Help Modules<b>
     <b>Prefixes:</b> <code>{cmd}</code></b>
     <b>Commands: {len(CMD_HELP)}</b>
    """
    if prev_match:
        curr_page = int(prev_match[1])
        await callback_query.edit_message_text(
            text=prev_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    next_text = f"""
    <b>Help Modules<b>
     <b>Prefixes:</b> <code>{cmd}</code></b>
     <b>Commands: {len(CMD_HELP)}</b>
    """
    if next_match:
        next_page = int(next_match[1])
        await callback_query.edit_message_text(
            text=next_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    back_text = f"""
    <b>Help Modules<b>
     <b>Prefixes:</b> <code>{cmd}</code></b>
     <b>Commands: {len(CMD_HELP)}</b>
    """
    if back_match:
        await callback_query.edit_message_text(
            text=back_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, CMD_HELP, "help")),
            disable_web_page_preview=True,
        )

    
       
@app.on_message(filters.command(["user"]) & filters.private)
async def usereee(_, message):
    user_id = message.from_user.id
    if user_id not in (OWNER, DEVS):
        return await message.reply(
            "❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya OWNER yang bisa menggunakan perintah ini"
        )
    count = 0
    user = ""
    for X in botlist:
        try:
            count += 1
            user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
 ╰ ID: <code>{X.me.id}</code>
"""
        except BaseException:
            pass
    if len(str(user)) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")


@app.on_callback_query(filters.regex("^alv_cls"))
async def _(cln, cq): 
    cq.data.split()
    unPacked = unpackInlineMessage(cq.inline_message_id)
    for bot in botlist:
        if cq.from_user.id == int(bot.me.id):
            await bot.delete_messages(
                chat_id=unPacked.chat_id,
                message_ids=[unPacked.message_id]
            )
            


@app.on_callback_query(filters.regex("cl_ad"))
async def _(_, query: CallbackQuery):
    await query.message.delete()




@app.on_callback_query(filters.regex("inpo"))
async def _(_, query):
    await query.message.delete()
    await query.message.reply_text(
        text="<b> di sini saya dapat membantu anda menuju jalan ke surga klik tombol di bawah ini 👇</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [   
                    
                    InlineKeyboardButton(text="tutup", callback_data="cl_ad"),
                    InlineKeyboardButton("deak", url="http://my.telegram.org/auth"),
                ]
            ]
        ),
    )


@app.on_callback_query(filters.regex("restart"))
async def _(_, query: CallbackQuery):
    try:
        await query.edit_message_text("<b>Processing...</b>")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await asyncio.sleep(2)
    await query.edit_message_text(f"✅ <b>{app.me.mention} Berhasil Di Restart.</b>")
    args = [sys.executable, "-m", "naya"]
    execle(sys.executable, *args, environ)


@app.on_callback_query(filters.regex("retor"))
async def _(_, query: CallbackQuery):
    buttons = [
        [
            InlineKeyboardButton(text="✅ Restart", callback_data="restart"),
            InlineKeyboardButton("❌ Tidak", callback_data="cl_ad"),
        ],
    ]
    await query.edit_message_text(
        "<b>Apakah kamu yakin ingin Melakukan Restart ?</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_message(filters.command(["mstart"]))
async def _(_, message):
    user_id = message.from_user.id
    _ubot = [bot.me.id for bot in botlist]
    if user_id not in _ubot:
        return await message.reply_text(
            text=f"""
<b>👋 Hi <a href=tg://openmessage?user_id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a> !

<b>welcome to {app.me.mention}</b>
<b>Here I can help you deak </b>
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("bantuan", callback_data="help_back"),
                        InlineKeyboardButton(text="autodeak", callback_data="inpo"),
                    ]
                ]
            ),
        )
    else:
        await message.reply_text(
            text=f"""
<b>👋 Halo <a href=tg://openmessage?user_id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a> !
💭 Apa ada yang bisa saya bantuu ?
💡 Silakan pilih tombol dibawah untuk kamu perlukan.
</b>""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Pengaturan", callback_data="setong"),
                    ],
                    [InlineKeyboardButton("Tutup", callback_data="cl_ad")],
                ]
            ),
        )
