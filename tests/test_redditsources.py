import discord
import pytest

from cuteness.sources.redditcatloafs import RedditCatloafs
from cuteness.sources.redditcatpics import RedditCatpics
from cuteness.sources.redditcockatiel import RedditCockatiel
from cuteness.sources.redditfoxes import RedditFoxes
from cuteness.sources.redditpigs import RedditPigs
from cuteness.sources.redditraccoons import RedditRaccoons
from cuteness.sources.redditsquirrels import RedditSquirrels


@pytest.mark.asyncio
async def test_redditcatloafs():
    source = RedditCatloafs()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditcatpics():
    source = RedditCatpics()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditcockatiel():
    source = RedditCockatiel()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditfoxes():
    source = RedditFoxes()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditpigs():
    source = RedditPigs()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditraccoons():
    source = RedditRaccoons()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_redditsquirrels():
    source = RedditSquirrels()
    file = await source.fetch()
    assert isinstance(file, discord.File)
