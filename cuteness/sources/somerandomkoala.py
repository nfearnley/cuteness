import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class SomeRandomKoala(PicSource):
    category = "koala"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("https://some-random-api.ml/img/koala") as r:
                js = await r.json()
        image_url = js["link"]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, SomeRandomKoala())
