from naya.utils.db import mongo
from typing import Dict, List, Union 
from string import ascii_lowercase 


warnsdb = mongo["naya"]["warns"]
prefixes = mongo["naya"]["prefix"]

async def remove_warns(chat_id: int, name: str) -> bool:
    warnsd = await get_warns(chat_id)
    name = name.lower().strip()
    if name in warnsd:
        del warnsd[name]
        await warnsdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"warns": warnsd}},
            upsert=True,
        )
        return True
    return False 

async def add_warn(chat_id: int, name: str, warn: dict):
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    warns[name] = warn

    await warnsdb.update_one(
        {"chat_id": chat_id}, {"$set": {"warns": warns}}, upsert=True
    )

async def get_warns_count() -> dict:
    chats_count = 0
    warns_count = 0
    async for chat in warnsdb.find({"chat_id": {"$lt": 0}}):
        for user in chat["warns"]:
            warns_count += chat["warns"][user]["warns"]
        chats_count += 1
    return {"chats_count": chats_count, "warns_count": warns_count}


async def get_warns(chat_id: int) -> Dict[str, int]:
    warns = await warnsdb.find_one({"chat_id": chat_id})
    if not warns:
        return {}
    return warns["warns"]


async def get_warn(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    if name in warns:
        return warns[name]

async def int_to_alpha(user_id: int) -> str:
    alphabet = list(ascii_lowercase)[:10]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text
    
async def get_pref(user_id):
    sh = await prefixes.users.find_one({"_id": user_id})
    if sh:
        return sh.get("prefixesi")
    else:
        return "."

async def set_pref(user_id, prefix):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$set": {"prefixesi": prefix}}, upsert=True
    )


async def rem_pref(user_id):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$unset": {"prefixesi": ""}}, upsert=True
    )
