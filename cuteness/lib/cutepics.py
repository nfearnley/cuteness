import io
import mimetypes
import aiohttp
import random
import os.path
from urllib.parse import urlparse

from discord import File
from discord.ext.commands import command, Cog


def get_url_filename(url, content_type):
    filename = os.path.basename(urlparse(url).path)
    if mimetypes.guess_type(filename) != content_type:
        filename += mimetypes.guess_extension(content_type) or ""
    return


# download a file, saving it into a discord File object
async def download_file(url, session=None):
    if session is None:
        # If a session is not provided, create one and call download_file(url, session)
        async with aiohttp.ClientSession() as session:
            return await download_file(url, session)

    async with session.get(url) as r:
        if r.status != 200:
            raise PicFetchFailedException
        data = io.BytesIO(await r.read())
    filename = get_url_filename(url, r.content_type)
    return File(data, filename)


class PicFetchFailedException(Exception):
    pass


class PicCategoryCog(Cog, name="Cuteness"):
    def __init__(self, category):
        self.category = category
        self.fetch.name = category.name
        self.fetch.help = f"Get a random cute {category.name} picture"

    @command()
    async def fetch(self, ctx):
        picfile = await self.category.fetch()
        await ctx.channel.send(file=picfile)


class PicSource:
    category = None

    async def fetch(self):
        raise NotImplementedError()


class PicCategory:
    def __init__(self, name):
        self.name = name
        self.sources = []
        self.cog = PicCategoryCog(self)

    async def fetch(self):
        source = random.choice(self.sources)
        try:
            return await source.fetch()
        except Exception:
            raise PicFetchFailedException(f"Failed to fetch a pic from {self.name} category")

    def __len__(self):
        return len(self.sources)

    def add_source(self, source):
        self.sources.append(source)

    def remove_source(self, source):
        self.sources.remove(source)


class PicGetter:
    def __init__(self):
        self._categories = {}

    async def fetch(self, name=None):
        """fetch a random image from a category"""
        if name is None:
            name = random.choice(list(self._categories.keys()))
        name = name.lower()
        category = self._categories[name]
        return await category.fetch()

    def add_source(self, bot, source):
        name = source.category.lower()
        if name in self._categories:
            category = self._categories[name]
        else:
            category = PicCategory(name)
            bot.add_cog(category.cog)
            self._categories[name] = category
        category.add_source(source)

    def remove_source(self, bot, source):
        name = source.category.lower()
        category = self._categories[name]
        category.remove_source(bot, source)
        if len(category) > 0:
            return
        del self._categories[name]
        bot.remove_cog(category.cog)

    @property
    def categories(self):
        return list(self._categories.keys())


cutepics = PicGetter()
