import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class ShibaCats(PicSource):
    category = "cat"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("http://shibe.online/api/cats") as r:
                js = await r.json()
        image_url = js[0]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, ShibaCats())
