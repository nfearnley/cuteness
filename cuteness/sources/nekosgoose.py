from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class NekosGoose(JsonSource):
    category = "goose"
    url = "https://nekos.life/api/v2/img/goose"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosGoose())
