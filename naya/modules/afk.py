__MODULE__ = "afk"
__HELP__ = """
 bantuan untuk afk

  • perintah: <code>{0}afk</code>
  • penjelasan: untuk mengaktifkan afk

  • perintah: <code>{0}unafk</code>
  • penjelasan: untuk menonaktifkan afk
"""

from . import *


from naya.utils.db import * 

from time import time as waktunya

start_time = waktunya()

async def get_time(seconds):
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["detik", "menit", "jam", "hari", "ᴡ", "ᴍᴏ"]

    while count < 6:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        elif count < 4:
            remainder, result = divmod(seconds, 24)
        elif count < 5:
            remainder, result = divmod(seconds, 7)
        else:
            remainder, result = divmod(seconds, 30 * 24 * 60 * 60)

        if seconds == 0 and remainder == 0:
            break

        time_list.append(int(result))
        seconds = int(remainder)

    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]

    if len(time_list) >= 4:
        up_time += time_list.pop() + ":"

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


from time import time

afk_sanity_check: dict = {}
afkstr = """
#AFK Aktif\n Alasan {}
"""
onlinestr = """
#AFK Tidak Aktif\nAlasan {}
"""


async def is_afk_(f, client, message):
    user_id = client.me.id
    af_k_c = await check_afk(user_id)
    return bool(af_k_c)


is_afk = filters.create(func=is_afk_, name="is_afk_")


@bots.on_message(filters.me & filters.command("afk", cmd))
async def set_afk(client, message):
    if len(message.command) == 1:
        return await eor(
            message,
            f"<b>Gunakan format dengan berikan alasan</b>\n\n<b>Contoh</b> : <code>afk berak</code>",
        )
    user_id = client.me.id
    botlog = await get_log_groups(user_id)
    pablo = await eor(message, "<code>Processing...</code>")
    msge = None
    msge = get_text(message)
    start_1 = get_time.now()
    afk_start = start_1.replace(microsecond=0)
    if msge:
        msg = f"<b>❏ Sedang AFK</b>.\n<b> ╰ Alasan</b> : <code>{msge}</code>"
        await client.send_message(botlog, afkstr.format(msge))
        await go_afk(user_id, afk_start, msge)
    else:
        msg = "<b>❏ Sedang AFK</b>."
        await client.send_message(botlog, afkstr.format(msge))
        await go_afk(user_id, afk_start)
    await pablo.edit(msg)


@bots.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def afk_er(client, message):
    user_id = client.me.id
    if not message:
        return
    if not message.from_user:
        return
    if message.from_user.id == user_id:
        return
    use_r = int(user_id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 50:
        await message.reply_text("<b>❏ Sedang AFK</b>.")
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 50:
        return
    lol = await check_afk(user_id)
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = get_time.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    message_to_reply = (
        f"<b>❏ Sedang AFK</b>\n<b> ├ Waktu</b> :<code>{afk_runtime}</code>\n<b> ╰ Alasan</b> : <code>{reason}</code>"
        if reason
        else f"<b>❏ Sedang AFK</b>\n<b> ╰ Waktu</b> :<code>{afk_runtime}</code>"
    )
    await message.reply(message_to_reply)


@bots.on_message(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message):
    user_id = client.me.id
    botlog = await get_log_groups(user_id)
    back_alivee = get_time.now()
    afk_start = user_id["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(
        f"<b>❏ Saya Kembali.</b>\n<b> ╰ AFK Selama</b> : <code>{afk_runtime}</code>"
    )
    await kk.delete()
    await no_afk(user_id)
    await client.send_message(botlog, onlinestr.format(afk_runtime))












