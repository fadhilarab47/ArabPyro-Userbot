# Credits: @mrismanaziz recode by @Arabnihnge
# Copyright (C) 2024 ArabPyro-Userbot
#
# t.me/SiArab_Support & t.me/Arabc0de

import aiohttp


async def expand_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://expandurl.com/api/v1/?url={url}") as resp:
            expanded = await resp.text()

        return expanded if expanded != "false" and expanded[:-1] != url else None
