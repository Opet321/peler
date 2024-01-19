# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from . import *

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = (await app.get_chat_member(chat_id, user_id)).privileges
    if not member:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_video_chats:
        perms.append("can_manage_video_chats")
    return perms 


@bots.on_message(filters.command(["rmwarns"], cmd) & filters.me)
async def remove_warnings(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a message to remove a user's warnings."
        )
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    chat_id = message.chat.id
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if warns == 0 or not warns:
        await message.reply_text(f"{mention} have no warnings.")
    else:
        await remove_warns(chat_id, await int_to_alpha(user_id))
        await message.reply_text(f"Removed warnings of {mention}.")




@bots.on_message(filters.command(["warns"], cmd) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    warns = await get_warn(message.chat.id, await int_to_alpha(user_id))
    mention = (await client.get_users(user_id)).mention
    if warns:
        warns = warns["warns"]
    else:
        return await message.reply_text(f"{mention} has no warnings.")
    return await message.reply_text(f"{mention} has {warns}/3 warnings.")


@app.on_callback_query(filters.regex("unwarn_"))
async def unwarn_user(client, callback_query):
    chat_id = callback_query.message.chat.id
    permissions = await member_permissions(chat_id, client.me.id)  # Mengambil izin bot
    permission = "can_restrict_members"
    if permission not in permissions:
        return await callback_query.answer(
            "I don't have enough permissions to perform this action.\n"
            + f"Permission needed: {permission}",
            show_alert=True,
        )

    user_id = int(callback_query.data.split("_")[1])  # Mengambil user_id dari callback data
    warns = await get_warn(chat_id, await int_to_alpha(user_id))

    if warns and warns["warns"] > 0:  # Memeriksa apakah ada peringatan yang harus dihapus
        warn = {"warns": warns["warns"] - 1}
        await add_warn(chat_id, await int_to_alpha(user_id), warn)

        # Memperbarui pesan dengan tambahan informasi bahwa peringatan telah dihapus
        text = callback_query.message.text.markdown
        text = f"{text}\n\n__Warn removed by {client.me.mention}__"
        await callback_query.message.edit(text)
    else:
        await callback_query.answer("User has no warnings.")

@bots.on_message(filters.me & filters.command(["setgpic"], cmd))
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await eor(message, f"`Kamu bukan admin di {message.chat.title}")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await eor(message, "`Balas ke photo untuk set!`")


@bots.on_message(filters.command(["warn", "dwarn"], cmd) & filters.me)
async def member_warn(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    chat_id = message.chat.id
    if not user_id:
        return await eor(message, "I can't find that user.")
    if user_id == client.me.id:
        return await message.edit(
            "I can't warn myself, i can leave if you want."
        )
    if user_id in DEVS:
        return await message.edit(
            "You Wanna Warn The Elevated One?, RECONSIDER!"
        )
    if user_id in (await list_admins(client, message.chat.id)):
        return await message.edit(
            "I can't warn an admin, You know the rules, so do i."
        )
    user, warns = await asyncio.gather(
        client.get_users(user_id),
        get_warn(chat_id, await int_to_alpha(user_id)),
    )
    mention = user.mention
    keyboard = ikb({"🚨  Remove Warn  🚨": f"unwarn_{user_id}"})
    if warns:
        warns = warns["warns"]
    else:
        warns = 0
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if warns >= 2:
        await message.chat.ban_member(user_id)
        await message.edit(
            f"Number of warns of {mention} exceeded, BANNED!"
        )
        await remove_warns(chat_id, await int_to_alpha(user_id))
    else:
        warn = {"warns": warns + 1}
        msg = f"""
**Warned User:** {mention}
**Warned By:** {message.from_user.mention if message.from_user else 'Anon'}
**Reason:** {reason or 'No Reason Provided.'}
**Warns:** {warns + 1}/3"""
        await message.edit(msg, reply_markup=keyboard)
        await add_warn(chat_id, await int_to_alpha(user_id), warn)



@bots.on_message(filters.command(["ban", "dban"], cmd) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    ky = await eor(message, "`Processing...`")
    if not user_id:
        return await ky.edit("Tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await ky.edit("Tidak bisa banned diri sendiri.")
    if user_id in DEVS:
        return await ky.edit("Tidak bisa banned Devs!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ky.edit("Tidak bisa banned admin.")
    try:
        # await ky.delete()
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = f"<b>Banned User:</b> {mention}\n<b>Banned By:</b> {message.from_user.mention}\n"
    if reason:
        msg += f"<b>Reason:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await ky.edit(msg)
    except ChatAdminRequired:
        return await ky.edit("**Anda bukan admin di group ini !**")


@bots.on_message(filters.command(["unban"], cmd) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    zz = await eor(message, "`Processing...`")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await zz.edit("`Tidak bisa unban ch`")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await zz.edit("Berikan username, atau reply pesannya.")
    try:
        await message.chat.unban_member(user)
        await asyncio.sleep(0.1)
        # await zz.delete()
        umention = (await client.get_users(user)).mention
        await zz.edit(f"Unbanned! {umention}")
    except ChatAdminRequired:
        return await zz.edit("**Anda bukan admin di group ini !**")


@bots.on_message(filters.command(["pin", "unpin"], cmd) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await eor(message, "Balas ke pesan untuk pin/unpin .")
    await eor(message, "`Processing...`")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await eor(
            message,
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await eor(
            message,
            f"**Pinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await eor(message, "**Anda bukan admin di group ini !**")


@bots.on_message(filters.command(["mute", "dmute"], cmd) & filters.me)
async def mute(client, message):
    user_id, reason = await extract_user_and_reason(message)
    nay = await eor(message, "`Processing...`")
    if not user_id:
        return await nay.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await nay.edit("Tidak bisa mute diri sendiri.")
    if user_id in DEVS:
        return await nay.edit("Tidak bisa mute dev!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await nay.edit("Tidak bisa mute admin.")
    # await nay.delete()
    mention = (await client.get_users(user_id)).mention
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await nay.edit(msg)
    except ChatAdminRequired:
        return await nay.edit("**Anda bukan admin di group ini !**")


@bots.on_message(filters.command(["unmute"], cmd) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    kl = await eor(message, "`Processing...`")
    if not user_id:
        return await kl.edit("Pengguna tidak ditemukan.")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        # await kl.delete()
        umention = (await client.get_users(user_id)).mention
        await kl.edit(f"Unmuted! {umention}")
    except ChatAdminRequired:
        return await kl.edit("**Anda bukan admin di group ini !**")


@bots.on_message(filters.command(["kick", "dkick"], cmd) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    ny = await eor(message, "`Processing...`")
    if not user_id:
        return await ny.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await ny.edit("Tidak bisa kick diri sendiri.")
    if user_id == DEVS:
        return await ny.edit("Tidak bisa kick dev!.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ny.edit("Tidak bisa kick admin.")
    # await ny.delete()
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await ny.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await ny.edit("**Anda bukan admin di group ini !**")


@bots.on_message(
    filters.group & filters.command(["promote", "fullpromote"], cmd) & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    biji = await eor(message, "`Processing...`")
    if not user_id:
        return await biji.edit("Pengguna tidak ditemukan.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            await asyncio.sleep(1)
            # await biji.delete()
            umention = (await client.get_users(user_id)).mention
            return await biji.edit(f"Fully Promoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        # await biji.delete()
        umention = (await client.get_users(user_id)).mention
        await biji.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await biji.edit("**Anda bukan admin di group ini !**")


@bots.on_message(
    filters.group
    & filters.command(["cdemote"], [cmd])
    & filters.user(DEVS)
    & ~filters.me
)
@bots.on_message(filters.group & filters.command(["demote"], cmd) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    sempak = await eor(message, "`Processing...`")
    if not user_id:
        return await sempak.edit("Pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await sempak.edit("Tidak bisa demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    await asyncio.sleep(1)
    # await sempak.delete()
    umention = (await client.get_users(user_id)).mention
    await sempak.edit(f"Demoted! {umention}")


__MODULE__ = "admin"
__HELP__ = f"""
Bantuan Untuk Admin

• perintah: <code>{cmd}ban, dban or unban</code> [balas pesan atau berikan username]
• penjelasan: Untuk blokir, hapus pesan dengan blokir serta buka blokir

• perintah: <code>{cmd}pin or unpin</code> [balas pesan]
• penjelasan: Untuk menyematkan dan melepas sematan pesan grup.

• perintah: <code>{cmd}setgpic</code> [balas foto]
• penjelasan: Untuk mengubah foto grup.

• perintah: <code>{cmd}kick or dkick</code> [balas pesan atau berikan username]
• penjelasan: Untuk menendang atau hapus pesan dengan menendang pengguna.

• perintah: <code>{cmd}promote or fullpromote</code> [balas pesan atau berikan username]
• penjelasan: Untuk menjadikan admin digrup anda.

• perintah: <code>{cmd}mute or unmute</code> [balas pesan atau berikan username]
• penjelasan: Untuk membisukan atau membuka bisu pengguna digrup.
"""
