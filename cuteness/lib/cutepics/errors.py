class PicFetchFailedException(Exception):
    """Thrown when a category fails to download an image"""
    pass


class SourceNotReadyException(Exception):
    """Thrown when a source is not ready to fetch an image"""
    pass
