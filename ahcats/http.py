import asyncstdlib as asl
from typing import Tuple

import aiohttp
import yarl

from ahcats.utils import VALID_FORMATS

from .errors import HTTPError

BASE_URL = "https://http.cat/"


class HTTPClient():
    __slots__ = ["session"]

    def __init__(self) -> None:
        self.session = None

    async def _init_session(self) -> None:
        """Internal function used to initiate an aiohttp ClientSession
        """
        self.session = aiohttp.ClientSession(headers={
            'content-type': f'image/jpeg'
        })

    def _get_url(self, error_code: int) -> str:
        """Internal function to get the URL to be used in the 
        HTTP GET request to the HTTP Cat API

        :param error_code: the HTTP error code
        :type error_code: int
        :return: the url to send the HTTP GET request to
        :rtype: str
        """
        url = yarl.URL.build(
            scheme="https",
            host="http.cat/",
            path=f"/{str(error_code)}.jpg"
        )
        return str(url)

    @asl.lru_cache(maxsize=None)
    async def get(self, error_code: int) -> Tuple[bytes, str]:
        """Dispatch an HTTP GET request to HTTP Cat API

        :param error_code: the HTTP error code
        :type error_code: int
        :raises HTTPError: error raised if an error with the HTTP GET 
            request occurred
        :return: tuple containing the image bytes and its URL
        :rtype: Tuple[bytes, str]
        """
        url = BASE_URL + str(error_code) + ".jpg"
        if not self.session:
            await self._init_session()

        async with self.session.get(url) as response:
            if not 200 <= response.status < 300:
                raise HTTPError(url, response.status)
            data = await response.read()
        await self.close()
        return data, url

    async def close(self):
        """Internal function to close the active ClientSession, if not 
        already closed
        """
        if self.session:
            await self.session.close()
            self.session = None
