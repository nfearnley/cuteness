from cuteness.lib.cutepics import cutepics, JsonPicSource


class SomeRandomKoala(JsonPicSource):
    category = "koala"
    url = "https://some-random-api.ml/img/koala"
    json_path = "link"


def setup(bot):
    cutepics.add_source(bot, SomeRandomKoala())
