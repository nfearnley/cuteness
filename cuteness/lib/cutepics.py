import io
import mimetypes
import aiohttp
import random
import os.path
from urllib.parse import urlparse

from discord import File
from discord.ext.commands import command, Cog


def get_url_filename(url, mimetype):
    """Returns the correct filename, given url and mimetype

    The filename is extracted from the url.
    The mimetype is used to determine the appropriate file extension. If the extension is missing, it is appended to the filename.
    """
    filename = os.path.basename(urlparse(url).path)
    filename_mimetype, _ = mimetypes.guess_type(filename)
    if filename_mimetype != mimetype:
        mimetype_extension = mimetypes.guess_extension(mimetype)
        filename += mimetype_extension or ""
    return filename


async def download_file(url, session=None):
    """Downloads a file from a url, returning it as a discord.py File object

    If an existing session is not provided, one will be created.
    """
    if session is None:
        async with aiohttp.ClientSession() as session:
            return await download_file(url, session)

    async with session.get(url) as r:
        if r.status != 200:
            raise PicFetchFailedException
        data = io.BytesIO(await r.read())
    filename = get_url_filename(url, r.content_type)
    return File(data, filename)


class PicFetchFailedException(Exception):
    """Thrown when a category fails to download an image"""
    pass


class PicCategoryCog(Cog, name="Cuteness"):
    """A discord.py Cog used to dynamically create a new command for each category"""

    def __init__(self, category):
        self.category = category
        self.fetch.name = category.name
        self.fetch.help = f"Get a random cute {category.name} picture"

    @command()
    async def fetch(self, ctx):
        picfile = await self.category.fetch()
        await ctx.channel.send(file=picfile)


class PicSource:
    """A stub for creating child PicSource classes

    Each source belongs to a single category, and is used to fetch images for that category.
    Child classes must have `PicSource.category` set
    When a category tries to retrieve an image, it will call async `PicSource.fetch()`. This should be overridden by an child classes.
    """
    category = None

    async def fetch(self):
        raise NotImplementedError()


class PicCategory:
    """A class repesenting each category of images

    Sources will be added to this category by calling PicGetter.add_source()
    Images can be fetched from this category with PicCategory.fetch()
    """
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

    def add_source(self, source):
        self.sources.append(source)


class PicGetter:
    """Root class of cutepics module

    Accessible by: from cuteness.lib.cutepics import cutepics
    An image from a random category can be fetched with `cutepics.fetch()`
    An image from a specific category can be fetched with `cutepics.fetch(name)`
    Sources can be added with `cutepics.add_source(bot, source)`
    A list of categories is available from `cutepics.categories`
    """
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

    @property
    def categories(self):
        return list(self._categories.keys())


cutepics = PicGetter()
