from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class SomeRandomPanda(JsonSource):
    category = "panda"
    url = "https://some-random-api.ml/img/panda"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomPanda())
