import discord
import pytest

from cuteness.sources.swtiny import SWTiny


@pytest.mark.asyncio
async def test_swtiny():
    bot = None  # TODO: Replace with a mock bot
    source = SWTiny(bot)
    file = await source.fetch()
    assert isinstance(file, discord.File)
