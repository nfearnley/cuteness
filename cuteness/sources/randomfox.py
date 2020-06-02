import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, PicFetchFailedException


class RandomFoxSource(PicSource):
    def __init__(self):
        super().__init__("fox")

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://randomfox.ca/floof/") as r:
                if r.status != 200:
                    raise PicFetchFailedException
                js = await r.json()
        image_url = js["image"]
        return await self.download(image_url)


source = RandomFoxSource()


def setup(bot):
    cutepics.registerSource(bot, source)


def teardown(bot):
    cutepics.unregisterSource(bot, source)
