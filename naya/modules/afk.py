import time
import re 

from pyrogram import Client, filters, enums
from pyrogram.types import Message 
from pyrogram import raw 
from typing import Optional, Union, Callable
from functools import wraps 
from pyrate_limiter import BucketFullException, Duration, Limiter, RequestRate, MemoryListBucket
from pyrogram import utils
from pyrogram.errors import PeerIdInvalid

from . import * 

__MODULE__ = "afk"
__HELP__ = f"""
Bantuan Untuk Afk

• perintah: <code>{cmd}afk</code> [alasan]
• penjelasan: Untuk mengaktifkan mode afk.
"""

class RateLimiter:
    """
    Implement rate limit logic using leaky bucket
    algorithm, via pyrate_limiter.
    (https://pypi.org/project/pyrate-limiter/)
    """

    def __init__(self) -> None:
        # 2 requests per seconds
        self.second_rate = RequestRate(2, Duration.SECOND)

        # 15 requests per minute.
        self.minute_rate = RequestRate(15, Duration.MINUTE)

        # 500 requests per hour
        self.hourly_rate = RequestRate(500, Duration.HOUR)

        # 1500 requests per day
        self.daily_rate = RequestRate(1500, Duration.DAY)

        self.limiter = Limiter(
            self.minute_rate,
            self.hourly_rate,
            self.daily_rate,
            bucket_class=MemoryListBucket,
        )

    async def acquire(self, userid: Union[int, str]) -> bool:
        """
        Acquire rate limit per userid and return True / False
        based on userid ratelimit status.
        """

        try:
            self.limiter.try_acquire(userid)
            return False
        except BucketFullException:
            return True


def ratelimiter(func: Callable) -> Callable:
    """
    Restricts user's from spamming commands or pressing buttons multiple times
    using leaky bucket algorithm and pyrate_limiter.
    """

    @wraps(func)
    async def decorator(client: Client, update: Union[Message, CallbackQuery]):
        userid = update.from_user.id if update.from_user else update.sender_chat.id
        is_limited = await ratelimit.acquire(userid)

        if is_limited and userid not in warned_users:
            if isinstance(update, Message):
                await update.reply_text(warning_message)
                warned_users[userid] = 1
                return

            elif isinstance(update, CallbackQuery):
                try:
                    await update.answer(warning_message, show_alert=True)
                except QueryIdInvalid:
                    warned_users[userid] = 1
                    return
                warned_users[userid] = 1
                return

        elif is_limited and userid in warned_users:
            pass
        else:
            return await func(client, update)

    return decorator


def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await app.leave_chat(message.chat.id)
            return
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            error_feedback = split_limits(
                "**ERROR** | `{}` | `{}`\n\n```{}```\n\n```{}```\n".format(
                    0 if not message.from_user else message.from_user.id,
                    0 if not message.chat else message.chat.id,
                    message.text or message.caption,
                    "".join(errors),
                ),
            )
            for x in error_feedback:
                await app.send_message(LOG_GROUP_ID, x)
            raise err

    return capture


def get_readable_time2(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["detik", "menit", "jam", "hari", "bulan", "tahun", "y"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time



@bots.on_message(filters.command(["afk"], cmd))
async def active_afk(_, ctx: Message):
    if ctx.sender_chat:
        return 
    user_id = ctx.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time2((int(time.time() - timeafk)))
            if afktype == "animation":
                if str(reasonafk) == "None":
                    return await ctx.reply_animation(
                    data, 
                    caption=f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>",
                    )
                else:
                     return await ctx.reply_animation(
                     data,
                     caption=f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak</b><code>{seenago}</code>",
                     )
            if afktype == "photo":
                if str(reasonafk) == "None":  # Perhatikan koreksi ini
                    return await ctx.reply_photo(
                    photo=f"downloads/{user_id}.jpg",
                    caption=f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>\n\n<b>Alasan: </b> <code>{reasonafk}</code>",
                    )
                else:  
                     return await ctx.reply_photo(
                     photo=f"downloads/{user_id}.jpg",
                     caption=f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak </b> <code>{seenago}</code>",
                     )
            if afktype == "text":
                return await ctx.reply_text( 
                    f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>",
                       disable_web_page_preview=True,
                     )
            if afktype == "text_reason":
                return await ctx.reply_text( 
                    f"downloads/{user_id}.jpg",
                     caption=f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>",
                    
                    disable_web_page_preview=True,
                )
        except Exception as e:
            return await ctx.reply_text(f"{ctx.from_user.first_name} [<code>{ctx.from_user.id}</code>] <b>Kembali Online</b>",
                
                disable_web_page_preview=True,
            )
    if len(ctx.command) == 1 and not ctx.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(ctx.command) > 1 and not ctx.reply_to_message:
        _reason = (ctx.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(ctx.command) == 1 and ctx.reply_to_message.animation:
        _data = ctx.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(ctx.command) > 1 and ctx.reply_to_message.animation:
        _data = ctx.reply_to_message.animation.file_id
        _reason = (ctx.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(ctx.command) == 1 and ctx.reply_to_message.photo:
        await app.download_media(ctx.reply_to_message, file_name=f"{user_id}.jpg")
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(ctx.command) > 1 and ctx.reply_to_message.photo:
        await app.download_media(ctx.reply_to_message, file_name=f"{user_id}.jpg")
        _reason = ctx.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(ctx.command) == 1 and ctx.reply_to_message.sticker:
        if ctx.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(ctx.reply_to_message, file_name=f"{user_id}.jpg")
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(ctx.command) > 1 and ctx.reply_to_message.sticker:
        _reason = (ctx.text.split(None, 1)[1].strip())[:100]
        if ctx.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(ctx.reply_to_message, file_name=f"{user_id}.jpg")
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)
    await ctx.reply_text(f"{ctx.from_user.mention} [<code>{ctx.from_user.id}</code>] <b>Sekarang Afk</b>")
    


# Detect user that AFK based on Yukki Repo
@bots.on_message(
    filters.group & ~filters.me, & ~filters.private
    group=1,
)
async def afk_watcher_func(self: Client, ctx: Message):
    if ctx.sender_chat:
        return
    userid = ctx.from_user.id
    user_name = ctx.from_user.mention
    if ctx.entities:
        possible = ["/afk", f"/afk@{self.me.username}", "!afk"]
        message_text = ctx.text or ctx.caption
        for entity in ctx.entities:
            try:
                if (
                    entity.type == enums.MessageEntityType.BOT_COMMAND
                    and (message_text[0 : 0 + entity.length]).lower() in possible
                ):
                    return
            except UnicodeDecodeError:  # Some weird character make error
                return

    msg = ""
    replied_user_id = 0

    # Self AFK
    verifier, reasondb = await is_afk(userid)
    if verifier:
        await remove_afk(userid)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time2((int(time.time() - timeafk)))
            if afktype == "text":
                msg += f"{user_name} [<code>{userid}</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>"
            if afktype == "text_reason":
                msg += f"{user_name} [<code>{userid},</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>"
            if afktype == "animation":
                if str(reasonafk) == "None":
                    await ctx.reply_animation(
                        data,
                        caption=f"{user_name} [<code>{userid}</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>",
                        
                    )
                else:
                    await ctx.reply_animation(
                        data,
                        caption=f"{user_name} [<code>{userid}</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>",
                        )
                    
            if afktype == "photo":
                if str(reasonafk) == "None":
                    await ctx.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"{user_name} [<code>{userid}</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>",
                        
                    )
                else:
                    await ctx.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"{user_name} [<code>{userid}</code>] <b>kembali online dan telah afk selama</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>",
                        
                    )
        except:
            msg += f"{user_name} [<code>{userid}</code>] <b>kembali online</b>"

    # Replied to a User which is AFK
    if ctx.reply_to_message:
        try:
            replied_first_name = ctx.reply_to_message.from_user.mention
            replied_user_id = ctx.reply_to_message.from_user.id
            verifier, reasondb = await is_afk(replied_user_id)
            if verifier:
                try:
                    afktype = reasondb["type"]
                    timeafk = reasondb["time"]
                    data = reasondb["data"]
                    reasonafk = reasondb["reason"]
                    seenago = get_readable_time2((int(time.time() - timeafk)))
                    if afktype == "text":
                        msg += f"{replied_first_name} [<code>{replied_user_id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>"
                    if afktype == "text_reason":
                        msg += f"{replied_first_name} [<code>{replied_user_id}<code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>"
                        
                    if afktype == "animation":
                        if str(reasonafk) == "None":
                            send = await ctx.reply_animation(
                                data,
                                caption=f"{replied_first_name} [<code>{replied_user_id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>",
                            )
                        else:
                            send = await ctx.reply_animation(
                                data,
                                caption=f"{replied_first_name} [<code>{replied_user_id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>",
                            )
                    if afktype == "photo":
                        if str(reasonafk) == "None":
                            send = await ctx.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"{replied_first_name} [<code>{replied_user_id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>",
                            )
                        else:
                            send = await ctx.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"{replied_first_name} [<code>{replied_user_id}</code>] <b>Telah Afk Sejak</b> <code>{seenago}</code>\n\n<b>Alasan:</b> <code>{reasonafk}</code>",
                            )
                except Exception:
                    msg += f"{replied_first_name} [<code>{replied_user_id}</cod>] Sedang Afk",
                    
        except:
            pass

    # If username or mentioned user is AFK
    if ctx.entities:
        entity = ctx.entities
        j = 0
        for _ in range(len(entity)):
            if (entity[j].type) == enums.MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", ctx.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time2((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"{user.first_name[:25]} [`{userid}`] Telah Afk sejak `{seenago}` yang lalu"
                            
                        if afktype == "text_reason":
                            msg +=f"{user.first_name[:25]} [`{userid}`] Telah Afk Sejak `{seenago}` Yang Lalu\n\n Alasan: `{reasonafk}`"
                            
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await ctx.reply_animation(
                                    data,
                                    caption=f"{user.first_name[:25]} [`{userid}`] Telah Afk sejak `{seenago}` Yang lalu",
                                )
                            else:
                                send = await ctx.reply_animation(
                                    data,
                                    caption=f"{user.first_name[:25]} [`{userid}`] Telah Afk Sejak `{seenago}` Yang lalu\n\n Alasan: `{reasonafk}`",
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await ctx.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"{user.first_name[:25]} [`{userid}`] Telah Afk Sejak  `{seenago}` Yang lalu",
                                )
                            else:
                                send = await ctx.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"{user.first_name[:25]} [`{userid}`] Telah Afk sejak `{seenago}` yang lalu\n\n Alasan: `{reasonafk}`",
                                )
                    except:
                        msg += f"{user.first_name[:25]} [`{userid}`] Sedang Afk"
                        
            elif (entity[j].type) == enums.MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user_id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time2((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"{first_name[:25]} [`{user_id}`] Telah Afk sejak `{seenago}` Yang lalu"
                        if afktype == "text_reason":
                            msg += f"{first_name[:25]} [`{user_id}`] Telah Afk Sejak `{seenago}` Yang lalu\n\n Alasan: `{reasonafk}`"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await ctx.reply_animation(
                                    data,
                                    caption=f"{first_name[:25]} [`{user_id}`] Telah Afk sejak `{seenago}` Yang lalu",
                                )
                            else:
                                send = await ctx.reply_animation(
                                    data,
                                    caption=f"{first_name[:25]} [`{user_id}`] Telah Afk Sejak `{seenago}` Yang lalu\n\n Alasan: `{reasonafk}`",
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await ctx.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"{first_name[:25]} [`{user_id}`] Telah Afk sejak `{seenago}` Yang lalu",
                                )
                            else:
                                send = await ctx.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"{first_name[:25]} [`{user_id}`] Telah Afk Sejak `{seenago}` Yang lalu\n\n Alasan: `{reasonafk}`",
                                )
                    except:
                        msg += f"{first_name[:25]} [`{user_id}`] Sedang Afk"
            j += 1
    if msg != "":
        try:
            await ctx.reply_text(msg, disable_web_page_preview=True)
        except:
            return
    


              



                        