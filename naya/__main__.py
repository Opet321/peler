from platform import python_version as py
import aiorun

from naya.modules import *
from naya.utils import *
from naya.load import *
from naya.utils import *
from naya.utils.db import *
from naya.version import __version__ as nay
from naya.version import kynay_version as nan
from pyrogram import __version__ as pyro
from pyrogram import idle
from uvloop import install

from naya import *
from naya.config import *

MSG_ON = """
**Xel Premium Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
◉ **Kynaylibs** : `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Startup").info("Memulai Xel-Pyro Premium..")
    for bot in botlist:
        try:
            await bot.start() 
            ex = bot.me 
            user = ex.id
            await ajg(bot) 
            await babi(bot)
            botlog = await get_botlog(user)
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            try:
                await bot.send_message(botlog, MSG_ON.format(nan, py(), pyro, nay, cmd))
            except BaseException as a:
                LOGGER("Info").warning(f"{a}")

            ids.append(ex.id)   
            LOGGER("Info").info("Startup Completed")

        except Exception as e:
            LOGGER("X").info(f"{e}")
    await loadprem()
    await idle()
    await aiosession.close()

async def start_client() -> None:
    LOGGER("Logger").info("Starting the bot...")
    try:
        await app.start()
        with contextlib.suppress(TopicNotModified):
            await app.reopen_general_topic(FORUM_CHAT_ID)
    except RPCError as rpc_error:
        logger.error(str(rpc_error.MESSAGE))

    setattr(app, "db", Database(app))
    await app.db.connect()

    await app.set_bot_commands(
        commands=[
            BotCommand("del", "Delete by Reply"),
            BotCommand("start", "Show User Info"),
        ],
        scope=BotCommandScopeChatAdministrators(chat_id=FORUM_CHAT_ID),
    )

    LOGGER("Logger").info("Bot activated successfully.")


async def stop_client() -> None:
    LOGGER("Logger").info("Stopping the bot...")
    with contextlib.suppress(Exception):
        await app.close_general_topic(FORUM_CHAT_ID)
        await app.stop()

    await app.db.close()
    LOGGER("Logger").info("Bot stopped and database connection closed.")

if __name__ == "__main__": 
    aiorun.logger.disabled = True
    aiorun.run(start_client(), loop=app.loop, shutdown_callback=stop_client())
    install()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        LOGGER("Logger").info("Stopping Bot! GoodBye")
