from cuteness.lib.cutepics import cutepics, JsonPicSource


class SomeRandomFox(JsonPicSource):
    category = "fox"
    url = "https://some-random-api.ml/img/fox"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomFox())
