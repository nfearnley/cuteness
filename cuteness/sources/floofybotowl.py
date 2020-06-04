from cuteness.lib.cutepics import cutepics, JsonPicSource


class FloofyBotOwl(JsonPicSource):
    category = "owl"
    url = "http://pics.floofybot.moe/owl"
    json_path = "image"


def setup(bot):
    cutepics.add_source(bot, FloofyBotOwl())
