from cuteness.lib.cutepics import cutepics, RedditPicSource


class RedditSquirrels(RedditPicSource):
    category = "squirrel"
    subreddit = "squirrels"


def setup(bot):
    cutepics.add_source(bot, RedditSquirrels())
