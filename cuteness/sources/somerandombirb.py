from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class SomeRandomBirb(JsonSource):
    category = "bird"
    url = "https://some-random-api.ml/img/birb"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomBirb())
