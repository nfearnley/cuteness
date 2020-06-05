from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class TheCatApi(JsonSource):
    category = "cat"
    url = "https://api.thecatapi.com/v1/images/search"
    json_path = "[0].url"


def setup(bot):
    cutepics.add_source(bot, TheCatApi())
