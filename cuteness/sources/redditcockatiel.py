from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditCockatiel(RedditSource):
    category = "cockatiel"
    subreddit = "cockatiel"


def setup(bot):
    cutepics.add_source(bot, RedditCockatiel())
