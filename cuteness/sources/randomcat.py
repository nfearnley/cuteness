import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, PicFetchFailedException


class RandomCatSource(PicSource):
    def __init__(self):
        super().__init__("cat")

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://aws.random.cat/meow") as r:
                if r.status != 200:
                    raise PicFetchFailedException
                js = await r.json()
        image_url = js["file"]
        return await self.download(image_url)


source = RandomCatSource()


def setup(bot):
    cutepics.registerSource(bot, source)


def teardown(bot):
    cutepics.unregisterSource(bot, source)
