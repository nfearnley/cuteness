import asyncio
import random

from cuteness.lib.utils import find_one
from .errors import PicFetchFailedException

# TODO: add sources for: bat, rat, mouse, goat, llama, alpaca, pigeon, parrot, turtle, rabbit/bunny, horse, snake, penguin, sloth
category_aliases = {
    "bird": ["birds", "birb", "birbs", "birdy", "birdie", "birdies"],
    "cat": ["cats", "kitten", "kittens", "kitty", "kitties", "feline"],
    "cockatiel": ["cockatiels", "cockatoo", "cockatoos", "parrot", "parrots"],
    "dog": ["dogs", "doggo", "doggos", "doggy", "doggie", "doggies", "doge", "puppy", "puppies", "pup", "pups", "pupper", "puppers", "puppo", "canine", "canines", "pooch", "pooches"],
    "duck": ["ducks", "ducky", "duckies", "duckling", "ducklings"],
    "fox": ["foxes"],
    "goose": ["geese"],
    "koala": ["koalas"],
    "lizard": ["lizards", "reptile", "reptiles", "iguana", "iguanas", "gecko", "geckos"],
    "owl": ["owls", "owlet", "owlets"],
    "panda": ["pandas"],
    "pig": ["pigs", "piggy", "piggies", "piglet", "piglets"],
    "raccoon": ["racoons", "trashpanda", "trashpandas"],
    "redpanda": ["redpandas"],
    "squirrel": ["squirrels"],
    "tiny": ["tinies", "sw"]
}


class PicCategory:
    """A class repesenting each category of images

    This is a Cog used to dynamically create a new command for each category.
    Sources will be added to this category by calling PicGetter.add_source()
    Images can be fetched from this category with PicCategory.fetch()
    """

    def __init__(self, name):
        self.name = name
        self.aliases = category_aliases.get(name, [])
        self.sources = []
        prefetch_count = 1
        self.fetch_cache = asyncio.Queue(maxsize=prefetch_count)

    async def start(self):
        asyncio.create_task(self.prefetch())

    async def prefetch(self):
        """Automatically prefetch images for each category"""
        while True:
            try:
                print(f"Prefetching an image for {self.name!r} category")
                sources = self.sources.copy()
                random.shuffle(sources)
                file = None
                # Try all possible sources (in a random order) until we have at least one that succeeds
                while file is None and sources:
                    source = sources.pop()
                    try:
                        file = await source.fetch()
                    except Exception as e:
                        print(f"Failed to prefetch a image from {source.name!r} source in {self.name!r} category: {e}")
                if file is not None:
                    print(f"Successfully prefetched a image from {source.name!r} source in {self.name!r} category")
                    await self.fetch_cache.put(file)
                else:
                    print(f"Failed to find a source to prefetch an image in {self.name!r} category")
                    await asyncio.sleep(5)
            except Exception as e:
                print(f"Unexpected Exception during prefetch: {e}")

    async def fetch(self):
        # Try to get an image from the queue, waiting up for one second
        print(f"Fetching a image from {self.name!r} category")
        try:
            file = await asyncio.wait_for(self.fetch_cache.get(), timeout=0.5)
        except asyncio.TimeoutError:
            raise PicFetchFailedException(f"Failed to fetch a image from {self.name!r} category")
        print(f"Image fetched from {self.name!r} category")
        return file

    def add_source(self, source):
        self.sources.append(source)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PicCategory({self.name!r})"


class PicGetter:
    """Root class of cutepics module

    Accessible by: from cuteness.lib import cutepics
    An image from a random category can be fetched with `cutepics.fetch()`
    An image from a specific category can be fetched with `cutepics.fetch(name)`
    Sources can be added with `cutepics.add_source(bot, source)`
    A list of categories is available from `cutepics.categories`
    """

    def __init__(self):
        self._categories = []

    async def fetch(self, name=None):
        """fetch a random image from a category"""
        category = self.get_category(name)
        if category is None:
            raise KeyError(f"Unrecognized Category: {name}")
        return await category.fetch()

    def add_source(self, bot, source):
        name = source.category.lower()
        category = self.get_category(name, strict=True)
        if category is None:
            category = self.add_category(bot, name)
        category.add_source(source)

    def add_category(self, bot, name):
        category = PicCategory(name)
        self._categories.append(category)
        bot.add_listener(category.start, name="on_first_ready")
        return category

    def get_category(self, name, strict=False):
        if name is None:
            category = random.choice(self._categories)
        else:
            name = name.lower()
            category = find_one(c for c in self._categories if name == c.name)
            if not category and not strict:
                category = find_one(c for c in self._categories if name in c.aliases)
        return category

    @property
    def categories(self):
        return [c.name for c in self._categories]

    @property
    def categories_and_aliases(self):
        names = []
        for c in self._categories:
            names.append(c.name)
            names.extend(c.aliases)
        return names

    def __str__(self):
        return "cutepics"

    def __repr__(self):
        return "PicGetter"


cutepics = PicGetter()
