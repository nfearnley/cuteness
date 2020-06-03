import asyncio
import random

from cuteness.lib.cutepics import cutepics, PicSource, download_file


class SWTinySource(PicSource):
    category = "tiny"
    name = "swtiny"

    def __init__(self, bot):
        self.bot = bot
        self.image_urls = []
        bot.add_listener(self.on_first_ready)

    async def on_first_ready(self):
        asyncio.create_task(self.scrape_channel())

    async def fetch(self):
        image_url = random.choice(self.image_urls)
        return await download_file(image_url)

    async def scrape_channel(self):
        """Scrape the channel for unspoilered attachments"""
        channel = self.bot.get_channel(557317063644020787)
        running = True
        before = None
        while running:
            await asyncio.sleep(5)
            print("Scraping the next 200 message from #webfinds-sfw")
            next_before = None
            async for m in channel.history(limit=200, before=before):
                next_before = m.id
                self.image_urls.extend(a.url for a in m.attachments if not a.is_spoiler())
            print(f"{len(self.image_urls)} urls available from #webfinds-sfw")

            if next_before is None:
                running = False


def setup(bot):
    cutepics.add_source(bot, SWTinySource(bot))
