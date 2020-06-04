from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditRaccoons(RedditPicSource):
    category = "raccoon"
    subreddit = "Raccoons"


def setup(bot):
    cutepics.add_source(bot, RedditRaccoons())
