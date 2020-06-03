from cuteness.lib.cutepics import cutepics, JsonPicSource


class RandomDuk(JsonPicSource):
    category = "duck"
    url = "https://random-d.uk/api/random"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, RandomDuk())
