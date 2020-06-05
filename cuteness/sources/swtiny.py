from cuteness.lib import cutepics
from cuteness.lib.cutepics import DiscordSource


# TODO: Setup persistent file cache for image_urls
class SWTiny(DiscordSource):
    category = "tiny"
    channelid = 557317063644020787


def setup(bot):
    cutepics.add_source(bot, SWTiny(bot))
