import sys
from typing import Any

import aiohttp
import asyncstdlib as asl

from .http import HTTPClient
from .image import HCImage
from .utils import VALID_FORMATS



class Client():
    __slots__ = ['default_format', '_http_client', 'other_kwargs']

    def __init__(self, *, default_format: str = None,
                 session: aiohttp.ClientSession = None, **kwargs):
        """Instantantiates an ahcats Client instance

        :param default_format: a valid image format, defaults to None
        :type default_format: str, optional
        :param session: an active aiohttp.ClientSession, defaults to None
        :type session: aiohttp.ClientSession, optional
        """
        if default_format and not default_format.lower() in VALID_FORMATS:
            self.default_format = "jpg"
        else:
            self.default_format = default_format
        self._http_client = session or HTTPClient()
        self.other_kwargs = kwargs

    @asl.lru_cache(maxsize=None)
    async def get_image(self, error_code: int) -> HCImage:
        """Access the HTTP Cat API to retrieve an image based on the
        HTTP error code

        :param error_code: the HTTP error code
        :type error_code: int
        :return: instance of HCImage
        :rtype: HCImage
        """
        response, url = await self._http_client.get(error_code)
        return HCImage(url, error_code, response, format=self.default_format)


if int(sys.version_info[0]) < 3:
    raise ImportError(
        "Your version of Python is not supported. Please upgrade to Python 3"
    )

if __name__ == "__main__":
    raise ImportError(
        "This module must be imported instead of directly run"
    )
