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

class AwayFromKeyboard:
    def __init__(self, client, message, reason=""):  # Perbaiki dari init ke __init__
        self.client = client
        self.message = message
        self.reason = reason


@bots.on_message(filters.command(["afk"], cmd) & filters.me)
async def _(client, message): 
    user_id = client.me.id
    reason = get_arg(message)
    afk_handler = AwayFromKeyboard(client, message, reason)
    
    db_afk = {"time": time(), "reason": reason}  # Ganti self.reason dengan reason
    msg_afk = (
        f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴀʟᴀsᴀɴ: {reason}</blockquote></b>"
        if reason
        else "<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ</blockquote></b>"
    )
    
    await set_var(user_id, "AFK", db_afk)
    await message.reply(msg_afk, disable_web_page_preview=True)
    return await message.delete()


@bots.on_message(
    (filters.mentioned | filters.private)
    & ~filters.bot
    & ~filters.me
    & filters.incoming 
)
async def handle_message(client, message):
    user_id = await get_var(client.me.id, "AFK")  # Ambil data AFK
    if user_id:  # Pastikan untuk menggunakan user_id, bukan var
        lol = await check_afk(user_id)  # Dapatkan data AFK terlebih dahulu
        
        if lol is None:  # Periksa apakah lol adalah None
            return  # Atau Anda bisa memberikan respons lain jika diperlukan
        
        afk_time = lol.get("time")  # Gunakan .get() untuk menghindari KeyError
        afk_reason = lol.get("reason")
        
        if afk_time is not None:
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ├ ᴡᴀᴋᴛᴜ: {afk_runtime}\n ╰ ᴀʟᴀsᴀɴ: {afk_reason}</blockquote></b>"
                if afk_reason
                else f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴡᴀᴋᴛᴜ: {afk_runtime}</blockquote></b>"
            )
            return await message.reply(afk_text, disable_web_page_preview=True)
        else:
            # Tindakan jika afk_time tidak tersedia
            return await message.reply("Tidak ada informasi waktu AFK.", disable_web_page_preview=True)

@bots.on_message(filters.command(["unafk"], cmd) & filters.me)
async def unset_afk(client, message): 
    user_id = client.me.id
    afk_handler = AwayFromKeyboard(client, message)
    user_id = await get_var(user_id, "AFK")
    afk_time = user_id["time"]
    afk_runtime = await get_time(time() - afk_time)
    afk_text = f"<b>❏ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n ╰ ᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}"
    await afk_text.delete()
    await no_afk(user_id)
    await client.send_message(botlog, onlinestr.format(total_afk_time))











