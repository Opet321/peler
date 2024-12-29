__MODULE__ = "afk"
__HELP__ = """
 bantuan untuk afk

  • perintah: <code>{0}afk</code>
  • penjelasan: untuk mengaktifkan afk

  • perintah: <code>{0}unafk</code>
  • penjelasan: untuk menonaktifkan afk
"""

from . import *

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

    async def set_afk(self):
        db_afk = {"time": time(), "reason": self.reason}
        msg_afk = (
            f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴀʟᴀsᴀɴ: {self.reason}</blockquote></b>"
            if self.reason
            else "<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ</blockquote></b>"
        )
        await set_var(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk, disable_web_page_preview=True)
        return await self.message.delete()

    async def get_afk(self):
        vars = await get_var(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ├ ᴡᴀᴋᴛᴜ: {afk_runtime}\n ╰ ᴀʟᴀsᴀɴ: {afk_reason}</blockquote></b>"
                if afk_reason
                else f"<b><blockquote>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴡᴀᴋᴛᴜ: {afk_runtime}</blockquote></b>"
            )
            return await self.message.reply(afk_text, disable_web_page_preview=True)

    async def unset_afk(self):
        vars = await get_var(self.client.me.id, "AFK") 
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<b><blockquote>❏ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n ╰ ᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}</blockquote></b>"
            await self.message.reply(afk_text)
            await self.message.delete() 
            user_id = self.message.from_user.id
            await no_afk(user_id)


@bots.on_message(filters.command(["afk"], cmd) & filters.me)
async def _(client, message):
    reason = get_arg(message)
    afk_handler = AwayFromKeyboard(client, message, reason)
    await afk_handler.set_afk()


@bots.on_message(
    (filters.mentioned | filters.private)
    & ~filters.bot
    & ~filters.me
    & filters.incoming 
)
async def handle_message(client, message):
    afk_handler = AwayFromKeyboard(client, message)
    await afk_handler.get_afk()


@bots.on_message(filters.command(["unafk"], cmd) & filters.me)
async def _(client, message):
    afk_handler = AwayFromKeyboard(client, message)
    return await afk_handler.unset_afk()
