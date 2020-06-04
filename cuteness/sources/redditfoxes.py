from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditFoxes(RedditPicSource):
    category = "fox"
    subreddit = "foxes"


def setup(bot):
    cutepics.add_source(bot, RedditFoxes())
