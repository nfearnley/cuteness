from cuteness.lib import cutepics
from cuteness.lib.cutepics import JsonSource


class RandomDog(JsonSource):
    category = "dog"
    url = "https://random.dog/woof.json"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, RandomDog())
