import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class ShibaShibes(PicSource):
    category = "dog"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("http://shibe.online/api/shibes") as r:
                js = await r.json()
        image_url = js[0]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, ShibaShibes())
