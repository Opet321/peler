"""
✅ Edit Code Boleh
❌ Hapus Credits Jangan
THANKS TO TOMI
👤 Telegram: @T0M1_X
"""
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import os
import asyncio
import requests
import time
from datetime import datetime
from urllib.request import urlretrieve
from asyncio import get_event_loop
from functools import partial

import wget
from pyrogram import *
from pyrogram.types import *
from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch
from pytube import YouTube
from yt_dlp import YoutubeDL

from . import *

__MODULE__ = "youtube"
__HELP__ = f"""
Bantuan Untuk Youtube

• perintah: <code>{cmd}song</code> [judul]
• penjelasan: Untuk mendownload lagu dari youtube.

• perintah: <code>{cmd}video</code> [judul]
• penjelasan: Untuk mendownload video dari youtube.
"""


async def download_song(m, message, vid_id):
    try:
        m = await m.edit(text="Downloading...")
        link = YouTube(f"https://youtu.be/{vid_id}")
        title = link.title
        thumbloc = f"downloads/{title}.jpg"
        thumb = requests.get(link.thumbnail_url, allow_redirects=True)
        open(thumbloc, 'wb').write(thumb.content)
        songlink = link.streams.filter(only_audio=True).first()
        down = songlink.download(output_path="downloads/")
        first, last = os.path.splitext(down)
        song = first + '.mp3'
        os.rename(down, song)
        
        m = await m.edit(text="Uploading...")
        await message.reply_audio(audio=song, caption="", thumb=thumbloc)
        
        await m.delete()
        os.remove(song)
        os.remove(thumbloc)
    except Exception as e:
        await m.edit(f"Terjadi kesalahan. ⚠️ \nAnda juga bisa mendapatkan bantuan dari @kynansupport.__\n\n{str(e)}")
    except HTTPError as e:
        if e.status_code == 429:
            time.sleep(3)
            return await download_song(m, message, vid_id)
        else:
            raise e




async def download_video(m, message, vid_id):
    try:
        m = await m.edit(text="Downloading...")
        link = YouTube(f"https://youtu.be/{vid_id}")
        video_link = link.streams.get_highest_resolution()
        video = video_link.download(output_path="downloads/")
        
        m = await m.edit(text="Uploading...")
        await message.reply_video(video)
        
        await m.delete()
        os.remove(video)
    except Exception as e:
        await m.edit(f"Terjadi kesalahan. ⚠️ \nAnda juga bisa mendapatkan bantuan dari @kynansupport.__\n\n{str(e)}")
    except HTTPError as e:
        if e.status_code == 429:
            time.sleep(3)
            return await download_video(m, message, vid_id)
        else:
            raise e

@bots.on_message(filters.me & filters.command("song", cmd))
async def song_down(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            return await message.edit_text("Beri nama lagu ⚠️")
        
        m = await message.edit_text("Mencari ...")
        name = message.text.split(None, 1)[1]
        search_result = YoutubeSearch(name, max_results=1).to_dict()

        if search_result:
            vid_id = search_result[0]["id"]
            await download_song(m, message, vid_id)
        else:
            await m.edit(f"Tidak ditemukan {message.from_user.mention}. Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!")
    except Exception as e:
        await m.edit(f"""
Tidak ditemukan {message.from_user.mention}
Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!
    """)

@bots.on_message(filters.me & filters.command("video", cmd))
async def video_down(client: Client, message: Message):
    try:
        if len(message.command) < 2:
            return await message.edit_text("Beri nama lagu ⚠️")
        
        m = await message.edit_text("Mencari ...")
        name = message.text.split(None, 1)[1]
        search_result = YoutubeSearch(name, max_results=1).to_dict()

        if search_result:
            vid_id = search_result[0]["id"]
            await download_video(m, message, vid_id)
        else:
            await m.edit(f"Tidak ditemukan {message.from_user.mention}. Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!")
    except Exception as e:
        await m.edit(f"""
Tidak ditemukan {message.from_user.mention}
Silakan periksa, Anda menggunakan format yang benar atau ejaan Anda benar dan coba lagi!
    """)
