from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class RandomCat(JsonSource):
    category = "cat"
    url = "http://aws.random.cat/meow"
    json_path = "file"


def setup(bot):
    cutepics.add_source(bot, RandomCat())
