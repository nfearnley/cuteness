from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditPigs(RedditPicSource):
    category = "pig"
    subreddit = "pigs"


def setup(bot):
    cutepics.add_source(bot, RedditPigs())
