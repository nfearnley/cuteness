from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class NekosWoof(JsonSource):
    category = "dog"
    url = "https://nekos.life/api/v2/img/woof"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosWoof())
