from cuteness.lib.cutepics import cutepics, JsonPicSource


class RandomDog(JsonPicSource):
    category = "dog"
    url = "https://random.dog/woof.json"
    json_path = "url"


def setup(bot):
    cutepics.add_source(bot, RandomDog())
