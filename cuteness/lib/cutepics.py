import io
import mimetypes
import aiohttp
import random
import os.path
from urllib.parse import urlparse

from discord import File
from discord.ext.commands import command, Cog


class PicFetchFailedException(Exception):
    pass


class PicCategoryCog(Cog, name="Cuteness"):
    def __init__(self, bot, category):
        self.bot = bot
        self.category = category
        self.fetch.name = category.name
        self.fetch.help = f"Get a random cute {category.name} picture"

    @command()
    async def fetch(self, ctx):
        picfile = await self.category.fetch()
        await ctx.channel.send(file=picfile)


class PicSource:
    def __init__(self, category):
        self.category = category

    async def fetch(self):
        raise NotImplementedError()

    async def download(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status != 200:
                    raise PicFetchFailedException
                data = await r.read()
        filename = os.path.basename(urlparse(url).path)
        if mimetypes.guess_type(filename) != r.content_type:
            filename += mimetypes.guess_extension(r.content_type) or ""
        filedata = io.BytesIO(data)
        return File(filedata, filename)


class PicCategory:
    def __init__(self, bot, name):
        self.name = name
        self.sources = []
        self.cog = PicCategoryCog(bot, self)

    async def fetch(self):
        source = random.choice(self.sources)
        return await source.fetch()

    def __len__(self):
        return len(self.sources)

    def registerSource(self, source):
        self.sources.append(source)

    def unregisterSource(self, source):
        self.sources.remove(source)


class PicGetter:
    def __init__(self):
        self._categories = {}

    def registerSource(self, bot, source):
        name = source.category.lower()
        if name in self:
            category = self._categories[name]
        else:
            category = PicCategory(bot, name)
            bot.add_cog(category.cog)
            self._categories[name] = category
        category.registerSource(source)

    def unregisterSource(self, bot, source):
        name = source.category.lower()
        category = self._categories[name]
        category.unregisterSource(bot, source)
        if len(category) > 0:
            return
        del self._categories[name]
        bot.remove_cog(category.cog)

    async def fetch(self, name=None):
        """fetch a random image from a category"""
        if name is None:
            name = random.choice(list(self._categories.keys()))
        name = name.lower()
        category = self._categories[name]
        return await category.fetch()

    def __contains__(self, name):
        return name is None or name.lower() in self._categories


cutepics = PicGetter()
