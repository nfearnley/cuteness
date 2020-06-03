from cuteness.lib.cutepics import cutepics, JsonPicSource


class SomeRandomPanda(JsonPicSource):
    category = "panda"
    url = "https://some-random-api.ml/img/panda"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomPanda())
