from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditFoxes(RedditSource):
    category = "fox"
    subreddit = "foxes"


def setup(bot):
    cutepics.add_source(bot, RedditFoxes())
