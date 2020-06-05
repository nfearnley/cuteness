from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class TheDogApi(JsonSource):
    category = "dog"
    url = "https://api.thedogapi.com/v1/images/search"
    json_path = "[0].url"


def setup(bot):
    cutepics.add_source(bot, TheDogApi())
