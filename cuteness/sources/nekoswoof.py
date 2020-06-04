from cuteness.lib.cutepics import cutepics, JsonPicSource


class NekosWoof(JsonPicSource):
    category = "dog"
    url = "https://nekos.life/api/v2/img/woof"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, NekosWoof())
