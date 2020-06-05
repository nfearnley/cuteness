import aiohttp

from cuteness.lib.pathdict import PathDict
from ..utils import download_file
from ..errors import SourceNotReadyException
from .picsource import PicSource


class RedditSource(PicSource):
    """A special class of PicSource for downloading images from a subreddit"""
    subreddit = None
    maxtrycount = 5

    async def fetch(self):
        if self.subreddit is None:
            raise NotImplementedError

        trycount = 1
        file = None
        while file is None:
            if trycount > self.maxtrycount:
                raise SourceNotReadyException("No images found on this subreddit")
            async with aiohttp.ClientSession(raise_for_status=True) as session:
                async with session.get(f"https://api.reddit.com/r/{self.subreddit}/random") as r:
                    js = await r.json()
                    pdict = PathDict(js)
            if pdict["[0].data.children[0].data.post_hint"] == "image":
                image_url = pdict["[0].data.children[0].data.url"]
                file = await download_file(image_url)
            trycount += 1
        return file
