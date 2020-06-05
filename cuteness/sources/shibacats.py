from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class ShibaCats(JsonSource):
    category = "cat"
    url = "http://shibe.online/api/cats"
    json_path = "[0]"


def setup(bot):
    cutepics.add_source(bot, ShibaCats())
