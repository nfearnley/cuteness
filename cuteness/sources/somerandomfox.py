from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class SomeRandomFox(JsonSource):
    category = "fox"
    url = "https://some-random-api.ml/img/fox"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomFox())
