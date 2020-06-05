from cuteness.lib import cutepics
from cuteness.lib.cutepics import RedditSource


class RedditRaccoons(RedditSource):
    category = "raccoon"
    subreddit = "Raccoons"


def setup(bot):
    cutepics.add_source(bot, RedditRaccoons())
