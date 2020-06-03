from cuteness.lib.cutepics import cutepics, JsonPicSource


class TheDogApi(JsonPicSource):
    category = "dog"
    url = "https://api.thedogapi.com/v1/images/search"
    json_path = "[0].url"


def setup(bot):
    cutepics.add_source(bot, TheDogApi())
