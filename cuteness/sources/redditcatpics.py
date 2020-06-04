from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditCatpics(RedditPicSource):
    category = "cat"
    subreddit = "catpics"


def setup(bot):
    cutepics.add_source(bot, RedditCatpics())
