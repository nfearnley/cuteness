import os
import mimetypes
from urllib.parse import urlparse
import aiohttp
import io

from discord import File
from .errors import PicFetchFailedException


def get_url_filename(url, mimetype):
    """Returns the correct filename, given url and mimetype

    The filename is extracted from the url.
    The mimetype is used to determine the appropriate file extension. If the extension is missing, it is appended to the filename.
    """
    filename = os.path.basename(urlparse(url).path)
    if mimetype == "application/octet-stream":
        return filename
    filename_mimetype, _ = mimetypes.guess_type(filename)
    if filename_mimetype != mimetype:
        mimetype_extension = mimetypes.guess_extension(mimetype)
        filename += mimetype_extension or ""
    return filename


async def download_file(url, session=None):
    """Downloads a file from a url, returning it as a discord.py File object

    If an existing session is not provided, one will be created.
    """
    if session is None:
        async with aiohttp.ClientSession() as session:
            return await download_file(url, session)

    async with session.get(url) as r:
        if r.status != 200:
            raise PicFetchFailedException
        data = io.BytesIO(await r.read())
    filename = get_url_filename(url, r.content_type)
    return File(data, filename)
