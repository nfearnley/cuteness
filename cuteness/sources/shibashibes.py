from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class ShibaShibes(JsonSource):
    category = "dog"
    url = "http://shibe.online/api/shibes"
    json_path = "[0]"


def setup(bot):
    cutepics.add_source(bot, ShibaShibes())
