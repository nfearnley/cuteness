from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class RandomDuk(JsonSource):
    category = "duck"
    url = "https://random-d.uk/api/random"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, RandomDuk())
