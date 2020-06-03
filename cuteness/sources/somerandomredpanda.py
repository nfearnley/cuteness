from cuteness.lib.cutepics import cutepics, JsonPicSource


class SomeRandomRedPanda(JsonPicSource):
    category = "redpanda"
    url = "https://some-random-api.ml/img/red_panda"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomRedPanda())
