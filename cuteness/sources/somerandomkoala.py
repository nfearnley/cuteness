from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class SomeRandomKoala(JsonSource):
    category = "koala"
    url = "https://some-random-api.ml/img/koala"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomKoala())
