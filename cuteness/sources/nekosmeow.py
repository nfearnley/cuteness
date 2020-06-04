from cuteness.lib.cutepics import cutepics, JsonPicSource


class NekosMeow(JsonPicSource):
    category = "cat"
    url = "https://nekos.life/api/v2/img/meow"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosMeow())
