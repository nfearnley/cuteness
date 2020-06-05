from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class NekosMeow(JsonSource):
    category = "cat"
    url = "https://nekos.life/api/v2/img/meow"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosMeow())
