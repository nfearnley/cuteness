import aiohttp

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class RandomDog(PicSource):
    category = "dog"

    async def fetch(self):
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get("https://random.dog/woof.json") as r:
                js = await r.json()
        image_url = js["url"]
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, RandomDog())
