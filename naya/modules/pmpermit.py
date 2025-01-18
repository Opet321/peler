# @Rizzvbss | @Kenapanan | @SharingUserbot | Zaid-Userbot
# © @KynanSupport
import asyncio

from pyrogram import Client, filters
from pyrogram.raw.functions.messages import DeleteHistory 
from pyrogram.raw import functions
from asyncio import sleep
from pyrogram import *
from pyrogram.types import * 
from uuid import uuid4
from pyrogram.types import InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, InlineQuery, Message
from pyrogram.types import Message

from . import *

PM_GUARD_WARNS_DB = {}
PM_GUARD_MSGS_DB = {}

DEFAULT_TEXT = """
**𝗮𝗴𝗮𝗿 𝘀𝗶𝗹𝗮𝘁𝘂𝗿𝗮𝗵𝗺𝗶 𝘁𝗶𝗱𝗮𝗸 𝘁𝗲𝗿𝗽𝘂𝘁𝘂𝘀 𝗽𝗶𝗻𝗷𝗲𝗺 𝗱𝘂𝗹𝘂 𝘀𝗲𝗿𝗮𝘁𝘂𝘀**
"""

PM_WARN = """
{}
**𝗮𝗻𝗱𝗮 𝗺𝗲𝗺𝗶𝗹𝗶𝗸𝗶 `{}/{}` 𝗽𝗲𝗿𝗶𝗻𝗴𝗮𝘁𝗮𝗻**
"""

LIMIT = 5


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


async def is_antipm_(f, client, message):
    user_id = client.me.id
    antipm_c = await check_antipm(user_id)
    if antipm_c:
        return bool(True)
    else:
        return bool(False)

is_antipm = filters.create(func=is_antipm_, name="is_antipm_")

@bots.on_message(filters.command(["autopurge"], cmd) & filters.me)
async def set_antipm(client, message):
    try:
        if len(message.command) < 2:
            await message.reply("Please specify 'on' or 'off'.", quote=True)
            return
        
        if message.command[1] == "on":
            user_id = client.me.id
            await go_antipm(user_id)
            await message.reply("<b>Anti-PM activated!!</b>", quote=True)
        elif message.command[1] == "off":
            user_id = client.me.id
            await no_antipmk(user_id)
            await message.reply("<b>Anti-PM deactivated!!</b>", quote=True)
        else:
            kontols = await check_antipm(client.me.id)
            kurukuru = kontols.get("antipm", "False")
            await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)
    except Exception as e:
        print(f"Error in set_antipm: {e}")
        kontols = await check_antipm(client.me.id)
        kurukuru = kontols.get("antipm", "False")
        await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)


@bots.on_message(
   ~filters.me & ~filters.bot & filters
     .private & is_antipm 
)
async def handle_antipm(client: Client,
  message: Message) -> None: 
    if message.from_user.is_contact is True:
        return 
    if message.from_user.is_support is True:
        return 
    if message.from_user.id == OWNER: 
        return
      
    results = await client.get_inline_bot_results("@Tawassuthbot",  query="pmpermit") 
    await client.send_inline_bot_result(message.chat.id, results.query_id, results.results[0].id)
    peer_id = await client.resolve_peer(message.chat.id)  
    await sleep (10) 
    for countdown in ["3", "2", "1"]:
        await msg.edit(countdown)
    await client.invoke(DeleteHistory(peer=peer_id, max_id=0, revoke=True))




@app.on_inline_query() 
async def handle_inline(client: Client, inline: InlineQuery) -> None: 
    inline_query = inline.query 
    if inline_query.strip().lower().split()[0] == "pmpermit": 
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="contact me", user_id=client.me.id)]] 
        ) 
        await inline.answer( 
            results=[InlineQueryResultArticle(
                id=str(uuid4()), 
                title="Pmpermit",
                input_message_content 
                  =InputTextMessageContent("<b><blockquote>Maaf saya tidak bisa menerima PM, Silahkan hubungi saya melalui bot, klik tombol di bawah ini</b></blockquote>"), 
                reply_markup=keyboard 
            )]
        )


        


@bots.on_message(filters.command(["pmpermit", "antipm"], cmd) & filters.me)
async def permitpm(client, message):
    user_id = client.me.id
    babi = await message.reply("`Processing...`")
    bacot = get_arg(message)
    if not bacot:
        return await babi.edit(f"**Gunakan Format : `{cmd[0]}pmpermit on or off`.**")
    is_already = await get_var(user_id, "ENABLE_PM_GUARD")
    if bacot.lower() == "on":
        if is_already:
            return await babi.edit("`PMPermit Sudah DiHidupkan.`")
        await set_var(user_id, "ENABLE_PM_GUARD", True)
        await babi.edit("**PMPermit Berhasil DiHidupkan.**")
    elif bacot.lower() == "off":
        if not is_already:
            return await babi.edit("`PMPermit Sudah DiMatikan.`")
        await set_var(user_id, "ENABLE_PM_GUARD", False)
        await babi.edit("**PMPermit Berhasil DiMatikan.**")
    else:
        await babi.edit(f"**Gunakan Format : `{cmd[0]}pmpermit on or off`.**")


@bots.on_message(filters.command(["ok", "a"], cmd) & filters.me)
async def approve(client, msg):
    babi = await msg.edit("Processing...")
    chat_type = msg.chat.type
    if chat_type == "me":
        return await babi.edit("Apakah anda sudah gila ?")
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not msg.reply_to_message.from_user:
            return await babi.edit("Balas ke pesan pengguna, untuk disetujui")
        user_id = msg.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = msg.chat.id
    else:
        return
    already_approved = await check_user_approved(user_id)
    if already_approved:
        await babi.edit("Manusia ini sudah Di Setujui Untuk mengirim pesan")
    await add_approved_user(user_id)
    if user_id in PM_GUARD_WARNS_DB:
        PM_GUARD_WARNS_DB.pop(user_id)
        try:
            await client.delete_messages(
                chat_id=user_id, message_ids=PM_GUARD_MSGS_DB[user_id]
            )
        except:
            pass
    await babi.edit("Baiklah, pengguna ini sudah disetujui untuk mengirim pesan.")
    await babi.delete()


@bots.on_message(filters.command(["no", "da"], cmd) & filters.me)
async def disapprove(client, message):
    babi = await message.edit("`Processing...`")
    chat_type = message.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message.from_user:
            return await babi.edit("`Balas ke pesan pengguna, untuk ditolak.`")
        user_id = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    already_apprvd = await check_user_approved(user_id)
    if not already_apprvd:
        await babi.edit(
            "`Manusia ini memang belum Di Setujui Untuk mengirim pesan.`"
        )
    await rm_approved_user(user_id)
    await babi.edit("**Baiklah, pengguna ini ditolak untuk mengirim pesan.**")
    await babi.delete()


@bots.on_message(filters.command(["setmsg"], cmd) & filters.me)
async def set_msg(client, message):
    babi = await message.reply("`Processing...`")
    user_id = client.me.id
    r_msg = message.reply_to_message
    args_txt = get_arg(message)
    if r_msg:
        if r_msg.text:
            pm_txt = r_msg.text
        else:
            return await babi.edit(
                "`Silakan balas ke pesan untuk dijadikan teks PMPermit !`"
            )
    elif args_txt:
        pm_txt = args_txt
    else:
        return await babi.edit(
            "`Silakan balas ke pesan atau berikan pesan untuk dijadikan teks PMPermit !\n**Contoh :** {cmd[0]}setmsg Halo saya anuan`"
        )
    await set_var(user_id, "CUSTOM_PM_TEXT", pm_txt)
    await babi.edit(f"**Pesan PMPemit berhasil diatur menjadi : `{pm_txt}`.**")


@bots.on_message(filters.command(["setlimit"], cmd) & filters.me)
async def set_limit(client, message):
    babi = await message.reply("`Processing...`")
    user_id = client.me.id
    args_txt = get_arg(message)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await babi.edit("`Silakan berikan untuk angka limit !`")
    else:
        return await babi.edit(
            f"`Silakan berikan pesan untuk dijadikan angka limit !\n**Contoh :** {PREFIX[0]}setlimit 5`"
        )
    await set_var(user_id, "CUSTOM_PM_WARNS_LIMIT", pm_warns)
    await babi.edit(f"**Pesan Limit berhasil diatur menjadi : `{args_txt}`.**")


@bots.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot,
    group=69,
)
async def handle_pmpermit(client, message):
    user_info = await client.resolve_peer(message.chat.id)
    user_id = client.me.id
    siapa = message.from_user.id
    biji = message.from_user.mention
    chat_id = message.chat.id
    botlog = await get_log_groups(user_id)
    is_pm_guard_enabled = await get_var(user_id, "ENABLE_PM_GUARD")
    if message.chat.id != 777000:
        if LOG_CHATS_.RECENT_USER != message.chat.id:
            LOG_CHATS_.RECENT_USER = message.chat.id
            if LOG_CHATS_.NEWPM:
                await LOG_CHATS_.NEWPM.edit(
                    LOG_CHATS_.NEWPM.text.replace(
                        "**💌 #NEW_MESSAGE**",
                        f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                    )
                )
                LOG_CHATS_.COUNT = 0
            LOG_CHATS_.NEWPM = await client.send_message(
                botlog,
                f"💌 <b><u>MENERUSKAN PESAN BARU</u></b>\n<b> • Dari :</b> {biji}\n<b> • User ID :</b> <code>{siapa}</code>\n",
                parse_mode=enums.ParseMode.HTML,
            )
        try:
            async for pmlog in client.search_messages(message.chat.id, limit=1):
                await pmlog.forward(botlog)
            LOG_CHATS_.COUNT += 1
        except BaseException:
            pass
    if not is_pm_guard_enabled:
        return
    in_user = message.from_user
    is_approved = await check_user_approved(in_user.id)
    if is_approved:
        return
    elif in_user.is_fake or in_user.is_scam:
        await message.reply("`Sepertinya anda mencurigakan...`")
        return await client.block_user(in_user.id)
    elif in_user.is_support or in_user.is_verified or in_user.is_self:
        return
    elif siapa in DEVS:
        try:
            await add_approved_user(chat_id)
            await client.send_message(
                chat_id,
                f"<b>Menerima Pesan Dari {biji} !!\nTerdeteksi Developer Dari Naya-Premium.</b>",
                parse_mode=enums.ParseMode.HTML,
            )
        except:
            pass
        return
    master = await client.get_me()
    getc_pm_txt = await get_var(user_id, "CUSTOM_PM_TEXT")
    getc_pm_warns = await get_var(user_id, "CUSTOM_PM_WARNS_LIMIT")
    custom_pm_txt = getc_pm_txt if getc_pm_txt else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if in_user.id in PM_GUARD_WARNS_DB:
        try:
            if message.chat.id in PM_GUARD_MSGS_DB:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=PM_GUARD_MSGS_DB[message.chat.id],
                )
        except:
            pass
        PM_GUARD_WARNS_DB[in_user.id] += 1
        if PM_GUARD_WARNS_DB[in_user.id] >= custom_pm_warns:
            await message.reply(
                f"`Saya sudah memberi tahu peringatan {custom_pm_warns}\nTunggu tuan saya menyetujui pesan anda, atau anda akan diblokir !`"
            )
            await asyncio.sleep(0)
            await client.send(
                functions.messages.DeleteHistory(peer=user_info, max_id=0, revoke=True)
            )
        else:
            rplied_msg = await message.reply(
                PM_WARN.format(
                    custom_pm_txt,
                    PM_GUARD_WARNS_DB[in_user.id],
                    custom_pm_warns,
                )
            )
    else:
        PM_GUARD_WARNS_DB[in_user.id] = 1
        rplied_msg = await message.reply(
            PM_WARN.format(
                custom_pm_txt,
                PM_GUARD_WARNS_DB[in_user.id],
                custom_pm_warns,
            )
        )
    PM_GUARD_MSGS_DB[message.chat.id] = [rplied_msg.id]


__MODULE__ = "antipm"
__HELP__ = f"""
Bantuan Untuk PM Permit

• perintah: <code>{cmd}pmpermit</code> [on atau off]
• penjelasan: Untuk menghidupkan atau mematikan antipm

• perintah: <code>{cmd}autopurge</code> [on atau off]
• penjelasan: Untuk menghidupkan atau mematikan autopurge

• perintah: <code>{cmd}setmsg</code> [balas atau berikan pesan]
• penjelasan: Untuk mengatur pesan antipm.

• perintah: <code>{cmd}setlimit</code> [angka]
• penjelasan: Untuk mengatur peringatan pesan blokir.

• perintah: <code>{cmd}ok or a</code>
• penjelasan: Untuk menyetujui pesan.

• perintah: <code>{cmd}no or da</code>
• penjelasan: Untuk menolak pesan.
"""
