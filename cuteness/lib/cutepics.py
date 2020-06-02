import mimetypes
import aiohttp
import random
import os
from urllib.parse import urlparse

from discord import File
from discord.ext.commands import Command


class PicFetchFailedException(Exception):
    pass


class PicSource:
    def __init__(self, category):
        self.category = category
        cutepics.registerSource(self)

    async def fetch(self):
        raise NotImplementedError()

    async def download(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status != 200:
                    raise PicFetchFailedException
                data = await r.read()
            filename = os.basename(urlparse(url).path)
            if mimetypes.guess_type(filename) != r.content_type:
                filename += mimetypes.guess_extensionr.content_type() or ""
        return File(data, filename)


class PicCommand(Command):
    def __init__(self, name, category):
        async def callback(bot, ctx):
            picfile = await category.fetch()
            await ctx.channel.send(file=picfile)
        super().__init__(name=name, callback=callback, help=f"Get a random cute {name} picture")


class PicCategory:
    def __init__(self):
        self.sources = []

    async def fetch(self):
        source = random.choose(self.sources)
        await source.fetch()

    def __len__(self):
        return len(self.sources)

    def registerSource(self, source):
        self.sources.append(source)

    def unregisterSource(self, source):
        self.sources.remove(source)


class PicCategoryCollection:
    def __init__(self):
        self.categories = []

    def get(self, name):
        if name is None:
            return random.choose(self.categories.values())
        name = name.lower()
        return self.categories[name]

    def create(self, bot, name):
        name = name.lower()
        self.categories[name] = PicCategory()
        bot.add_command(PicCommand(name, self))

    def getOrCreate(self, bot, name):
        name = name.lower()
        if name not in self.categories:
            self.create(bot, name)
        return self.categories[name]

    def remove(self, bot, name):
        del self.categories[name]

    def removeIfEmpty(self, bot, name):
        name = name.lower()
        category = self.categories.get(name)
        if category is None:
            return
        if len(category) > 0:
            return
        del self.categories[name]
        bot.remove_command(name)


class PicGetter:
    def __init__(self):
        self.categories = PicCategoryCollection()

    def registerSource(self, bot, source):
        category = self.categories.getOrCreate(bot, source.category)
        category.registerSource(source)

    def unregisterSource(self, bot, source):
        category = self.categories.get(source.category)
        if not category:
            return
        category.unregisterSource(source)
        self.categories.removeIfEmpty(bot, source.category)

    async def fetch(self, category_name=None):
        category = self.categories.get(category_name)
        return await category.fetch()


cutepics = PicGetter()
