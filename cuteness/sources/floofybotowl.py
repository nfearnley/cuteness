from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class FloofyBotOwl(JsonSource):
    category = "owl"
    url = "http://pics.floofybot.moe/owl"
    json_path = "image"


def setup(bot):
    cutepics.add_source(bot, FloofyBotOwl())
