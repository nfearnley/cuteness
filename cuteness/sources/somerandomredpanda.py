from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class SomeRandomRedPanda(JsonSource):
    category = "redpanda"
    url = "https://some-random-api.ml/img/red_panda"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomRedPanda())
