from asyncio import sleep  
from time import sleep 
from pyrogram import Client, filters 
from pyrogram.types import Message 
from pyrogram.types.input_message_content.reply_parameters import ReplyParameters
from motor.motor_asyncio import  AsyncIOMotorClient as MongoCli 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from naya.config import MONGO_URL, OWNER
from . import * 
 
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL) 
users = db.users  
mongo = MongoCli(MONGO_URL) 
messages = db.messages 
 
 
async def _message_id(message_id): 
 message_id = await messages.find_one({"forward_id": f"{message_id}"}) 
 return message_id 


 
@app.on_message(filters.command("start"))
async def _start(client: Client, message: Message):  
    await message.react([ReactionTypeEmoji(emoji="👍")])
    user_db = await users.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text(f"<b><blockquote>Hello, {message.from_user.mention}!\nAda yang bisa saya banting ?</b></blockquote>", message_effect_id=5104841245755180586)
        user_id = {"user_id": f"{message.from_user.id}"}
        await users.insert_one(user_id)
    else:
        await message.reply_text(f"<b><blockquote>Status by React\n👍: Delivered\n👀: Read\n✍: edited</blockquote></b>", message_effect_id=5104841245755180586)
 

@app.on_message(filters.chat(int(OWNER)))
async def _owner(client: Client, message: Message): 
    await message.react([ReactionTypeEmoji(emoji="❤️‍🔥")])
    last_msg = None  # Memberikan nilai awal untuk last_msg
    async for msg in messages.find():
        last_msg = msg

    if message.reply_to_message:
        message_id = await _message_id(message.reply_to_message.id)
        if message_id:
            sent_message = await message.copy(int(message_id['user_id']), reply_to_message_id=int(message_id['message_id']))
            await message.reply_text(f"<b><blockquote>terkirim ke {message_id['user_id']}</b></blockquote>",  reply_parameters=ReplyParameters(message_id=message.id)) 
            if last_msg and int(last_msg['user_id']) != int(message_id['user_id']):
                message_data = {
                    "forward_id": f"{message_id['forward_id']}",
                    "message_id": f"{message_id['message_id']}",
                    "user_id": f"{message_id['user_id']}"
                }
                await messages.insert_one(message_data)


    else:
        if last_msg:
            message_id = await _message_id(last_msg['forward_id'])
            if message_id:
                sent_message = await message.copy(int(message_id['user_id']))
                await message.reply_text(f"<b><blockquote>terkirim ke {message_id['user_id']}</b></blockquote>", reply_parameters=ReplyParameters(message_id=message.id)) 
                
 
 
@app.on_message(filters.all & filters.private & ~filters.me)
async def _user(client: Client, message: Message): 
    await message.react([ReactionTypeEmoji(emoji="👀")])
    user_db = await users.find_one({"user_id": f"{message.from_user.id}"})
    if not user_db:
        await message.reply_text("<b>You are not in the database, enter /start to use the bot!</b>", reply_parameters=ReplyParameter(reply_to_message_id=message.id))
    else:
        forwarded_message = await message.forward(OWNER)  
        chat_id = message.chat.id
        message_data = {"forward_id": f"{forwarded_message.id}",
                        "message_id": f"{message.id}",
                        "user_id": f"{message.from_user.id}"}
        await messages.insert_one(message_data)
        #message = await message.reply_text(f"<b>Pesan Anda telah terkirim!!</b>", reply_to_message_id=message.id, disable_notification=True)
        #await asyncio.sleep(3)
        #await message.delete()
        
    