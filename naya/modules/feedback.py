from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message 
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from naya.config import MONGO_URL
from . import *


owner = "5005266266"

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
users = db.users 
mongo = MongoCli(MONGO_URL)
messages = db.messages


async def _message_id(message_id):
	message_id = await messages.find_one({"forward_id": f"{message_id}"})
	return message_id

@app.on_message(filters.command(["start"]))
async def _start(client: Client, message: Message):
    user_db = await users.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text(f"<b>Hello, {message.from_user.mention}!</b>", reply_to_message_id=message.id)
        user_id = {"user_id": f"{message.from_user.id}"}
        await users.insert_one(user_id)
        await client.send_message(message.chat.id, "<b>Kirim saya pesan Anda dan saya akan meneruskannya!</b>")
    else:
        await message.reply_text("<b>Kirim saya pesan Anda dan saya akan meneruskannya!</b>", reply_to_message_id=message.id)


@app.on_message(filters.chat(int(owner)))
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
            await messages.insert_one(message_data)
        await sleep(5)
        await message.delete()

    else:
        message_id = await _message_id(message_id=last_msg['forward_id'])
        await message.copy(int(message_id['user_id']))
        message = await message.reply_text(f"<b>Pesan Anda telah terkirim ke {(message_id['user_id'])}</b>", reply_to_message_id=message.id, disable_notification=True)
        await sleep(5)
        await message.delete()


@app.on_message(filters.all & ~filters.incoming & ~filters.private & ~filters.me & ~filters.forwarded & ~filters.via_bot & ~filters.bot)
async def _user(client: Client, message: Message):
    user_db = await users.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text(f"<b>You are not in the database, enter /start to use the bot!</b>", reply_to_message_id=message.id)
    else:
        forwarded_message = await message.forward(owner)
        message_data = {"forward_id": f"{forwarded_message.id}",
                        "message_id": f"{message.id}",
                        "user_id": f"{message.from_user.id}"}
        await messages.insert_one(message_data)
        message = await message.reply_text(f"<b>Pesan Anda telah terkirim!</b>", reply_to_message_id=message.id, disable_notification=True)
        await sleep(5)
        await message.delete()
    
         