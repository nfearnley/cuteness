import asyncio
import random

from cuteness.lib.cutepics import cutepics, PicSource, download_file, SourceNotReadyException


class ChannelScraper:
    def __init__(self, bot, channelid):
        self.bot = bot
        self.channelid = channelid
        self.image_urls = []
        self.scrape_delay = 2       # How many seconds to wait between scrapes
        self.scrape_count = 200     # How many messages to fetch per scrape
        self.last_message = None    # The last message id scraped
        bot.add_listener(self.on_first_ready)

    async def on_first_ready(self):
        self.channel = self.bot.get_channel(557317063644020787)
        asyncio.create_task(self.loop())

    async def loop(self):
        """Scrape the channel for unspoilered attachments"""
        running = True
        while running:
            try:
                running = await self.scrape()
            except Exception as e:
                print(f"Error while scraping channel #{self.channel.name} ({self.channel.id}): {e}")
                pass
            await asyncio.sleep(self.scrape_delay)

    async def scrape(self):
        """Scrape the channel for unspoilered attachments"""
        print(f"Scraping the next {self.scrape_count} messages from #{self.channel.name}")
        messages = await self.channel.history(limit=self.scrape_count, before=self.last_message).flatten()
        if not messages:
            return False
        self.last_message = messages[-1].id
        attachments = [a for m in messages for a in m.attachments]
        urls = [a.url for a in attachments if not a.is_spoiler()]
        self.image_urls.extend(urls)
        print(f"Found {len(attachments)} urls ({len(self.image_urls)} total) in #{self.channel.name}")
        return True


# TODO: Setup persistent file cache for image_urls
class SWTiny(PicSource):
    category = "tiny"

    def __init__(self, bot):
        self.bot = bot
        self.scraper = ChannelScraper(bot, 557317063644020787)

    async def fetch(self):
        if not self.scraper.image_urls:
            raise SourceNotReadyException("No image urls scraped yet")
        image_url = random.choice(self.scraper.image_urls)
        return await download_file(image_url)


def setup(bot):
    cutepics.add_source(bot, SWTiny(bot))
