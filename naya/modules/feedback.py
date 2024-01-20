from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *


@bots.on_message(filters.command("start"))
async def _start(client: Client, message: Message):
    user_db = await usersdb.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text(f"<b>Hello, {message.from_user.mention}!</b>", reply_to_message_id=message.id)
        user_id = {"user_id": f"{message.from_user.id}"}
        await usersdb.insert_one(user_id)
        await client.send_message(message.chat.id, "<b>Kirim saya pesan Anda dan saya akan meneruskannya!</b>")
    else:
        await message.reply_text("<b>Kirim saya pesan Anda dan saya akan meneruskannya!</b>", reply_to_message_id=message.id)



@bots.on_message(
    filters.private & filters.user(DEVS) & filters.incoming & ~filters.service & ~filters.me & ~filters.bot,
    group=69,
)
async def _owner(client: Client, message: Message):
    last_msg = [_ async for _ in messages.find()][-1]
    if message.reply_to_message:
        message_id = await _message_id(message_id=message.reply_to_message.id)
        await message.copy(int(message_id['user_id']), reply_to_message_id=int(message_id['message_id']))
        message = await message.reply_text(f"<b>Pesan Anda telah terkirim ke {(message_id['user_id'])}</b>", reply_to_message_id=message.id, disable_notification=True)
        if int(last_msg['user_id']) != int(message_id['user_id']):
            message_data = {"forward_id": f"{message_id['forward_id']}",
                            "message_id": f"{message_id['message_id']}",
                            "user_id": f"{message_id['user_id']}"}
            await messagesdb.insert_one(message_data)
        await sleep(5)
        await message.delete()

    else:
        message_id = await _message_id(message_id=last_msg['forward_id'])
        await message.copy(int(message_id['user_id']))
        message = await message.reply_text(f"<b>Pesan Anda telah terkirim ke {(message_id['user_id'])}</b>", reply_to_message_id=message.id, disable_notification=True)
        await sleep(5)
        await message.delete()



@bots.on_message(
    filters.private & filters.user(DEVS) & filters.incoming & ~filters.service & ~filters.all & ~filters.bot & ~filters.me,
    group=69,
)
async def _user(client: Client, message: Message):
    user_db = await usersdb.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text(f"<b>You are not in the database, enter /start to use the bot!</b>", reply_to_message_id=message.id)
    else:
        forwarded_message = await message.forward(owner)
        message_data = {"forward_id": f"{forwarded_message.id}",
                        "message_id": f"{message.id}",
                        "user_id": f"{message.from_user.id}"}
        await messagesdb.insert_one(message_data)
        message = await message.reply_text(f"<b>Pesan Anda telah terkirim!</b>", reply_to_message_id=message.id, disable_notification=True)
        await sleep(5)
        await message.delete()
