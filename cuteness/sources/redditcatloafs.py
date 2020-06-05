from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditCatloafs(RedditSource):
    category = "cat"
    subreddit = "Catloafs"


def setup(bot):
    cutepics.add_source(bot, RedditCatloafs())
