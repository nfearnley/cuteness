import pytest
import discord

from cuteness.sources.dogceo import DogCeo
from cuteness.sources.nekosgoose import NekosGoose
from cuteness.sources.nekoslizard import NekosLizard
from cuteness.sources.nekosmeow import NekosMeow
from cuteness.sources.nekoswoof import NekosWoof
from cuteness.sources.randomcat import RandomCat
from cuteness.sources.randomdog import RandomDog
from cuteness.sources.randomduk import RandomDuk
from cuteness.sources.randomfox import RandomFox
from cuteness.sources.shibabirds import ShibaBirds
from cuteness.sources.shibacats import ShibaCats
from cuteness.sources.shibashibes import ShibaShibes
from cuteness.sources.somerandombirb import SomeRandomBirb
from cuteness.sources.somerandomfox import SomeRandomFox
from cuteness.sources.somerandomkoala import SomeRandomKoala
from cuteness.sources.somerandompanda import SomeRandomPanda
from cuteness.sources.somerandomredpanda import SomeRandomRedPanda
from cuteness.sources.thecatapi import TheCatApi
from cuteness.sources.thedogapi import TheDogApi


@pytest.mark.asyncio
async def test_dogceo():
    source = DogCeo()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_nekosgoose():
    source = NekosGoose()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_nekoslizard():
    source = NekosLizard()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_nekosmeow():
    source = NekosMeow()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_nekoswoof():
    source = NekosWoof()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_randomcat():
    source = RandomCat()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_randomdog():
    source = RandomDog()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_randomduk():
    source = RandomDuk()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_randomfox():
    source = RandomFox()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_shibabirds():
    source = ShibaBirds()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_shibacats():
    source = ShibaCats()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_shibashibes():
    source = ShibaShibes()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_somerandombirb():
    source = SomeRandomBirb()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_somerandomfox():
    source = SomeRandomFox()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_somerandomkoala():
    source = SomeRandomKoala()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_somerandompanda():
    source = SomeRandomPanda()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_somerandomredpanda():
    source = SomeRandomRedPanda()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_thecatapi():
    source = TheCatApi()
    file = await source.fetch()
    assert isinstance(file, discord.File)


@pytest.mark.asyncio
async def test_thedogapi():
    source = TheDogApi()
    file = await source.fetch()
    assert isinstance(file, discord.File)
