from naya.utils.db import mongo

antipmdb = mongo["naya"]["antipm"]
usersdb = mongo["tilil"]["peler"]
chatsdb = mongo["kanjat"]["tolol"]

async def go_antipm(user_id: int):
    user_data = await antipmdb.users.find_one({"user_id": user_id})
    if user_data:
        await antipmdb.users.update_one(
            {"user_id": user_id},
            {"$set": {"antipm": True}},
        )
    else:
        await antipmdb.users.insert_one(
            {"user_id": user_id, "antipm": True}
        )


async def no_antipmk(user_id: int):
    await antipmdb.users.delete_one({"user_id": user_id, "antipm": True})


async def check_antipm(user_id: int):
    user_data = await antipmdb.users.find_one({"user_id": user_id, "antipm": True})
    return user_data

async def is_afk(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if user:
        return (True, user.get("reason", ""))  # Jika 'reason' ditemukan, kembalikan nilainya. Jika tidak, kembalikan string kosong.
    else:
        return (False, {})


async def add_afk(user_id: int, mode):
    await usersdb.update_one(
        {"user_id": user_id}, {"$set": {"reason": mode}}, upsert=True
    )


async def remove_afk(user_id: int):
    user = await usersdb.find_one({"user_id": user_id})
    if user:
        return await usersdb.delete_one({"user_id": user_id})

async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})