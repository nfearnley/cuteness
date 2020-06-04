from cuteness.lib.cutepics import cutepics, JsonPicSource


class NekosLizard(JsonPicSource):
    category = "lizard"
    url = "https://nekos.life/api/v2/img/lizard"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosLizard())
