from .core import cutepics
from .sources.picsource import PicSource
from .sources.discordsource import DiscordSource
from .sources.jsonsource import JsonSource
from .sources.redditsource import RedditSource

exports = {
    "PicSource": PicSource,
    "DiscordSource": DiscordSource,
    "JsonSource": JsonSource,
    "RedditSource": RedditSource
}


def __getattr__(name):
    if name in exports:
        return exports[name]
    else:
        return getattr(cutepics, name)
