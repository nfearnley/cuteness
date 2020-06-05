from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class DogCeo(JsonSource):
    category = "dog"
    url = "https://dog.ceo/api/breeds/image/random"
    json_path = "message"


def setup(bot):
    cutepics.add_source(bot, DogCeo())
