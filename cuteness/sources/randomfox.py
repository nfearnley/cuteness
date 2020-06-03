import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class RandomFoxSource(PicSource):
    category = "fox"
    name = "randomfox"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("https://randomfox.ca/floof/") as r:
                js = await r.json()
        image_url = js["image"]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, RandomFoxSource())
