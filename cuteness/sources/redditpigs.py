from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditPigs(RedditSource):
    category = "pig"
    subreddit = "pigs"


def setup(bot):
    cutepics.add_source(bot, RedditPigs())
