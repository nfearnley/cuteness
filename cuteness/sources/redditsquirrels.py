from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditSquirrels(RedditSource):
    category = "squirrel"
    subreddit = "squirrels"


def setup(bot):
    cutepics.add_source(bot, RedditSquirrels())
