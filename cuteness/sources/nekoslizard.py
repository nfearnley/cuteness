from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class NekosLizard(JsonSource):
    category = "lizard"
    url = "https://nekos.life/api/v2/img/lizard"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosLizard())
