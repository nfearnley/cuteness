from cuteness.lib.cutepics import cutepics, JsonPicSource


class DogCeo(JsonPicSource):
    category = "dog"
    url = "https://dog.ceo/api/breeds/image/random"
    json_path = "message"


def setup(bot):
    cutepics.add_source(bot, DogCeo())
