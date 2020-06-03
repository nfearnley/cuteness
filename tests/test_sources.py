import pytest
import discord
import pkgutil
from importlib import import_module

from cuteness.lib.cutepics import PicGetter


def add_source(self, bot, source):
    add_source.value = source


PicGetter.add_source = add_source


class FakeBot():
    def __init__(self):
        self.uses_listener = False

    def add_listener(self, func):
        self.uses_listener = True


def generate_sources():
    sources = []
    for m in pkgutil.iter_modules(["cuteness/sources"]):
        module = import_module(f"cuteness.sources.{m.name}", package="cuteness")
        add_source.value = None
        bot = FakeBot()
        module.setup(bot)
        source = add_source.value
        if not hasattr(source, "bot") and not bot.uses_listener:
            sources.append(source)
    return sources


@pytest.fixture(params=generate_sources())
def source_fixture(request):
    return request.param


@pytest.mark.asyncio
async def test_source(source_fixture):
    file = await source_fixture.fetch()
    assert isinstance(file, discord.File)
