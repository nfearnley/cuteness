from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class RandomFox(JsonSource):
    category = "fox"
    url = "https://randomfox.ca/floof/"
    json_path = "image"


def setup(bot):
    cutepics.add_source(bot, RandomFox())
