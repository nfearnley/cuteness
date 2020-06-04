from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditCockatiel(RedditPicSource):
    category = "cockatiel"
    subreddit = "cockatiel"


def setup(bot):
    cutepics.add_source(bot, RedditCockatiel())
