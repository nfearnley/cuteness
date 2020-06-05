class PicSource:
    """A stub for creating child PicSource classes

    Each source belongs to a single category, and is used to fetch images for that category.
    Child classes must have `PicSource.category` set
    When a category tries to retrieve an image, it will call async `PicSource.fetch()`. This should be overridden by an child classes.
    """
    category = None

    async def fetch(self):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PicSource({self.name!r})"

    @property
    def name(self):
        return self.__class__.__name__
