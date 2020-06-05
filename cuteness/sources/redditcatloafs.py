from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditCatloafs(RedditPicSource):
    category = "cat"
    subreddit = "Catloafs"


def setup(bot):
    cutepics.add_source(bot, RedditCatloafs())
