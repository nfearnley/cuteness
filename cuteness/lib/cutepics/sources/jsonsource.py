import aiohttp

from cuteness.lib.pathdict import PathDict
from ..utils import download_file
from .picsource import PicSource


class JsonSource(PicSource):
    """A special class of PicSource for downloading images from a JSON api"""
    url = None
    json_path = None

    async def fetch(self):
        if self.url is None or self.json_path is None:
            raise NotImplementedError
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(self.url) as r:
                js = PathDict(await r.json())
        image_url = js[self.json_path]
        return await download_file(image_url)
