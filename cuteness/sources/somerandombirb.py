from cuteness.lib.cutepics import cutepics, JsonPicSource


class SomeRandomBirb(JsonPicSource):
    category = "bird"
    url = "https://some-random-api.ml/img/birb"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomBirb())
