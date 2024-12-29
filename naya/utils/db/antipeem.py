from naya.utils.db import mongo

antipmdb = mongo["naya"]["antipm"]

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