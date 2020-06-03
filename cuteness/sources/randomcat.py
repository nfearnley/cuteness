from cuteness.lib.cutepics import cutepics, JsonPicSource


class RandomCat(JsonPicSource):
    category = "cat"
    url = "http://aws.random.cat/meow"
    json_path = "file"


def setup(bot):
    cutepics.add_source(bot, RandomCat())
