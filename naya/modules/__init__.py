import sys
import asyncio
import pyrogram

from glob import glob
from os.path import basename, dirname, isfile

from pyrogram import *
from pyrogram.types import *

from naya import *
from naya.utils import *
from naya.utils.font_tool import *
from naya.utils.db import * 
from naya.utils.db.permit import *
from naya.utils.db.pref import *
from naya.utils.db.antipeem import *
from requests import get

from naya import *
from naya.utils import (
    time_formatter,)

from naya import (
    StartTime,)

BL_UBOT = [-1001303015845] 

DEVS = [ 
  5628376737,
  ]

async def ajg(client):
    try:
        await client.join_chat("bantenp")
    except pyrogram.errors.exceptions.bad_request_400.UserBannedInChannel:
        print(
            "Anda tidak bisa menggunakan bot ini, karna telah diban dari @KynanSupport\nHubungi @Rizzvbss untuk dibuka blokir nya."
        )
        sys.exit()

while 0 < 6:
    _BL_GCAST = get(
        "https://raw.githubusercontent.com/opet321/blacklist/master/blacklistgcast.json"
    )
    if _BL_GCAST.status_code != 200:
        if 0 != 5:
            continue
        BL_GCAST = [
            -1001812143750,
            -1001696368727,
            -1001704645461,
            -1001982790377,
            -1001885769033,
            -1001821201567,
            -1001473548283,
            -1001853283409,
            -1001287188817,
        ]
        break
    BL_GCAST = _BL_GCAST.json()
    break

del _BL_GCAST


def loadModule():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )
