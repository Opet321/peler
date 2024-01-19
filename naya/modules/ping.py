import time
from datetime import datetime
from random import choice
from time import time

from pyrogram import *
from pyrogram.raw.functions import Ping
from pyrogram.types import *

from . import *

TIME_DURATION_UNITS = (
    ("w", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount}{unit}{"" if amount == 1 else ""}')
    return ":".join(parts)


@bots.on_message(filters.command(["setemoji"], cmd) & filters.me)
async def change_emot(client, message):
    try:
        msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                "<b>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜ ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ</b>"
            )

        if len(message.command) < 3:
            return await msg.edit("<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")

        query_mapping = {"pong": "EMOJI_PING", "mention": "EMOJI_MENTION", "uptime": "EMOJI_UPTIME"}
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_var(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"<b>✅ <code>{query_var}</code> ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ</b>")
        else:
            await msg.edit("<b>ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    except Exception as error:
        await msg.edit(str(error))


@bots.on_message(filters.user(DEVS) & filters.command("Cping", "") & ~filters.me)
@bots.on_message(filters.command(["ping", "p"], cmd) & filters.me)
async def _(client, message):
    start = time.time()
    current_time = datetime.now()
    await client.invoke(Ping(ping_id=randint(0, 2147483647)))
    delta_ping = round((time.time() - start) * 1000, 3)
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    emot_1 = await get_var(client.me.id, "EMOJI_PING")
    emot_2 = await get_var(client.me.id, "EMOJI_UPTIME")
    emot_3 = await get_var(client.me.id, "EMOJI_MENTION")
    emot_pong = emot_1 if emot_1 else "5269563867305879894"
    emot_uptime = emot_2 if emot_2 else "6226371543065167427"
    emot_mention = emot_3 if emot_3 else "5323470315370585285"
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_pong}>🏓</emoji>Results:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={emot_uptime}>⏰</emoji>Uptime:</b> <code>{str(uptime).replace('.', ',')} ms</code>
<b><emoji id={emot_mention}>👑</emoji>Mention:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    else:
        _ping = f"""
<b>Results!:</b> {delta_ping} ms
<b>Uptime:</b> {uptime}
<b>Mention:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    await message.edit_text(_ping)
    await asyncio.sleep(60)
    await message.delete()

@app.on_callback_query(filters.regex("0_cls"))
async def now(_, cq):
    await cq.message.delete()
