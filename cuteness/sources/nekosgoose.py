from cuteness.lib.cutepics import cutepics, JsonPicSource


class NekosGoose(JsonPicSource):
    category = "goose"
    url = "https://nekos.life/api/v2/img/goose"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosGoose())
