import asyncio
import random

from .picsource import PicSource
from ..errors import SourceNotReadyException
from ..utils import download_file


class ChannelScraper:
    def __init__(self, bot, channelid, *, output):
        self.bot = bot
        self.channelid = channelid
        self.image_urls = output
        self.messages_scraped = 0
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
                print(f"Error while scraping channel #{self.channel} ({self.channel.id}): {e}")
                pass
            await asyncio.sleep(self.scrape_delay)
        if self.image_urls:
            print(f"Successfully scraped {len(self.image_urls)} urls in {self.messages_scraped} messages from #{self.channel}")
        else:
            print(f"Nothing to scrape from #{self.channel}")

    async def scrape(self):
        """Scrape the channel for unspoilered attachments"""
        print(f"Scraping the next {self.scrape_count} messages from #{self.channel}")
        messages = await self.channel.history(limit=self.scrape_count, before=self.last_message).flatten()
        self.messages_scraped += len(messages)
        if not messages:
            print("No message found")
            return False
        self.last_message = messages[-1].id
        attachments = [a for m in messages for a in m.attachments]
        urls = [a.url for a in attachments if not a.is_spoiler()]
        self.image_urls.extend(urls)
        print(f"Found {len(attachments)} urls ({len(self.image_urls)} total) in #{self.channel}")
        return True


class ChannelWatcher:
    def __init__(self, bot, channelid, *, output):
        self.channelid = channelid
        self.image_urls = output
        bot.add_listener(self.on_message)

    async def on_message(self, message):
        if message.channel.id != self.channelid:
            return
        self.scrape(message)

    async def scrape(self, message):
        urls = [a.url for a in message.attachments if not a.is_spoiler()]
        self.image_urls.extend(urls)
        print(f"Added {len(urls)} new urls ({len(self.image_urls)} total) from #{self.channel}")


# TODO: Setup persistent file cache for image_urls
class DiscordSource(PicSource):
    """A special class of PicSource for scraping images from discord"""
    category = None
    channelid = None

    def __init__(self, bot):
        if self.category is None or self.channelid is None:
            raise NotImplementedError
        self.image_urls = []
        self.bot = bot
        self.scraper = ChannelScraper(bot, self.channelid, output=self.image_urls)
        self.watcher = ChannelWatcher(bot, self.channelid, output=self.image_urls)

    async def fetch(self):
        if not self.scraper.image_urls:
            raise SourceNotReadyException("No image urls scraped yet")
        image_url = random.choice(self.scraper.image_urls)
        return await download_file(image_url)
