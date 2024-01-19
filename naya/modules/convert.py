import asyncio
import os
import shutil
from io import BytesIO

from pyrogram import filters
from py_extract import Video_tools
from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from . import *

__MODULE__ = "convert"
__HELP__ = f"""
Bantuan Untuk Convert

• perintah: <code>{cmd}toaudio</code> [reply to video]
• penjelasan: Untuk merubah video menjadi audio mp3.
           
• perintah: <code>{cmd}toanime</code> [reply to photo]
• penjelasan: Untuk merubah foto menjadi anime.

• perintah: <code>{cmd}toimg</code> [balas stikers]
• penjelasan: Untuk membuat nya menjadi foto.
"""

async def run_memek(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

mod_name = os.path.basename(__file__)[:-3]

@bots.on_message(filters.me & filters.command("toanime", cmd))
async def _(client, message):
    Tm = await eor(message, "<b>Tunggu sebentar...</b>")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                get_photo = message.reply_to_message.photo.file_id
            if message.reply_to_message.sticker:
                pass
            if message.reply_to_message.animation:
                pass
            path = await client.download_media(message.reply_to_message)
            with open(path, "rb") as f:
                content = f.read()
            os.remove(path)
            get_photo = BytesIO(content)
        elif message.command[1] in ["foto", "profil", "photo"]:
            chat = (
                message.reply_to_message.from_user
                or message.reply_to_message.sender_chat
            )
            get = await client.get_chat(chat.id)
            photo = get.photo.big_file_id
            get_photo = await client.download_media(photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                "Balas ke foto dan saya akan merubah foto anda menjadi anime"
            )
        get = await client.get_chat(message.command[1])
        photo = get.photo.big_file_id
        get_photo = await client.download_media(photo)
    await client.unblock_user("@qq_neural_anime_bot")
    Tm_S = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await Tm.edit("<b>Sedang diproses...</b>")
    await Tm_S.delete()
    await asyncio.sleep(30)
    info = await client.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in client.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(InputMediaPhoto(anime.photo.file_id))
    if anime_photo:
        await client.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await client.send_message(
            message.chat.id,
            f"<b>gagal merubah {file} menjadi gambar anime</b>",
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))


@bots.on_message(filters.me & filters.command(["toaudio"], cmd))
async def _(client, message):
    replied_msg = message.reply_to_message
    babi = await message.reply("`Downloading Video . . .`")
    ext_out_path = os.getcwd() + "/" + "downloads/py_extract/audios"
    if not replied_msg:
        await babi.edit("**Mohon Balas Ke Video**")
        return
    if not replied_msg.video:
        await babi.edit("**Mohon Balas Ke Video**")
        return
    if os.path.exists(ext_out_path):
        await babi.edit("`Processing.....`")
        return
    replied_video = replied_msg.video
    try:
        await babi.edit("`Downloading...`")
        ext_video = await client.download_media(message=replied_video)
        await babi.edit("`Extracting Audio(s)...`")
        exted_aud = Video_tools.extract_all_audio(input_file=ext_video, output_path=ext_out_path)
        await babi.edit("`Uploading...`")
        for nexa_aud in exted_aud:
            await message.reply_audio(audio=nexa_aud, caption=f"`Extracted by` {(await client.get_me()).mention}")
        await babi.edit("`Extracting Finished!`")
        shutil.rmtree(ext_out_path)
    except Exception as e:
        await babi.edit(f"**Error:** `{e}`")
