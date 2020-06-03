import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class TheDogApi(PicSource):
    category = "dog"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("https://api.thedogapi.com/v1/images/search") as r:
                js = await r.json()
        image_url = js[0]["url"]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, TheDogApi())
