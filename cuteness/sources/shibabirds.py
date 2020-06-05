from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class ShibaBirds(JsonSource):
    category = "bird"
    url = "http://shibe.online/api/birds"
    json_path = "[0]"


def setup(bot):
    cutepics.add_source(bot, ShibaBirds())
