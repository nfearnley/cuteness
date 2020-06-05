from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditCatpics(RedditSource):
    category = "cat"
    subreddit = "catpics"


def setup(bot):
    cutepics.add_source(bot, RedditCatpics())
