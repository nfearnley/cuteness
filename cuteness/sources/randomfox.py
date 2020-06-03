from cuteness.lib.cutepics import cutepics, JsonPicSource


class RandomFox(JsonPicSource):
    category = "fox"
    url = "https://randomfox.ca/floof/"
    json_path = "image"


def setup(bot):
    cutepics.add_source(bot, RandomFox())
