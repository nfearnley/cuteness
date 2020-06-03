from cuteness.lib.cutepics import cutepics, JsonPicSource


class ShibaCats(JsonPicSource):
    category = "cat"
    url = "http://shibe.online/api/cats"
    json_path = "0"


def setup(bot):
    cutepics.add_source(bot, ShibaCats())
