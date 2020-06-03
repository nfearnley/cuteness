from cuteness.lib.cutepics import cutepics, JsonPicSource


class TheCatApi(JsonPicSource):
    category = "cat"
    url = "https://api.thecatapi.com/v1/images/search"
    json_path = "[0].url"


def setup(bot):
    cutepics.add_source(bot, TheCatApi())
