import asyncio
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


class PicSource:
    """A stub for creating child PicSource classes

    Each source belongs to a single category, and is used to fetch images for that category.
    Child classes must have `PicSource.category` set
    When a category tries to retrieve an image, it will call async `PicSource.fetch()`. This should be overridden by an child classes.
    """
    category = None
    name = None

    async def fetch(self):
        raise NotImplementedError()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PicSource({self.name!r})"

    @property
    def name(self):
        return self.__class__.__name__


class PicCategory(Cog, name="Cuteness"):
    """A class repesenting each category of images

    This is a Cog used to dynamically create a new command for each category.
    Sources will be added to this category by calling PicGetter.add_source()
    Images can be fetched from this category with PicCategory.fetch()
    """

    def __init__(self, name):
        self.name = name
        self.sources = []
        prefetch_count = 1
        self.fetch_cache = asyncio.Queue(maxsize=prefetch_count)
        self.fetch_command.name = name
        self.fetch_command.help = f"Get a random cute {name} picture"

    @Cog.listener()
    async def on_first_ready(self):
        asyncio.create_task(self.prefetch())

    async def prefetch(self):
        """Automatically prefetch images for each category"""
        while True:
            try:
                print(f"Prefetching an image for {self.name!r} category")
                sources = self.sources.copy()
                random.shuffle(sources)
                file = None
                # Try all possible sources (in a random order) until we have at least one that succeeds
                while file is None:
                    if not sources:
                        break
                    source = sources.pop()
                    try:
                        file = await source.fetch()
                    except Exception as e:
                        print(f"Failed to prefetch a image from {source.name!r} source in {self.name!r} category: {e}")
                if file is not None:
                    await self.fetch_cache.put(file)
                    print(f"Successfully prefetched a image from {source.name!r} source in {self.name!r} category")
                else:
                    print(f"Failed to find a source to prefetch an image in {self.name!r} category")
                    await asyncio.sleep(5)
            except Exception as e:
                print(f"Unexpected Exception during prefetch: {e}")

    async def fetch(self):
        # Try to get an image from the queue, waiting up for one second
        print(f"Fetching a image from {self.name!r} category")
        try:
            file = await asyncio.wait_for(self.fetch_cache.get(), timeout=0.5)
        except asyncio.TimeoutError:
            raise PicFetchFailedException(f"Failed to fetch a image from {self.name!r} category")
        print(f"Image fetched from {self.name!r} category")
        return file

    @command()
    async def fetch_command(self, ctx):
        picfile = await self.fetch()
        await ctx.channel.send(file=picfile)

    def add_source(self, source):
        self.sources.append(source)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PicCategory({self.name!r})"


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
            self._categories[name] = category
            bot.add_cog(category)
        category.add_source(source)

    @property
    def categories(self):
        return list(self._categories.keys())

    def __str__(self):
        return "cutepics"

    def __repr__(self):
        return "PicGetter"


cutepics = PicGetter()
