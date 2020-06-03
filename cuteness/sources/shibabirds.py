from cuteness.lib.cutepics import cutepics, JsonPicSource


class ShibaBirds(JsonPicSource):
    category = "bird"
    url = "http://shibe.online/api/birds"
    json_path = "[0]"


def setup(bot):
    cutepics.add_source(bot, ShibaBirds())
