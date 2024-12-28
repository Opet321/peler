from platform import python_version as py

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


async def main() -> None:
    await app.start()
    LOGGER("Startup").info("Memulai Naya-Pyro Premium..")
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

 
async def starting_up():
    try:
        await loadprem()
        await idle()
    except BaseException as excp:
        LOGGER("Logger").info(excp)
    except KeyboardInterrupt:
        pass
    finally:
        LOGGER("Logger").info("Stopping Bot! GoodBye")
        loop.stop()
        await aiosession.close()

if __name__ == "__main__":
    install()
    loop.run_until_complete(main())
    try:
        asyncio.set_event_loop(loop)
        loop.create_task(starting_up())
        run(starting_up(), loop=loop, stop_on_unhandled_errors=True)
    except BaseException as excp:
        LOGGER("Logger").info(excp)
