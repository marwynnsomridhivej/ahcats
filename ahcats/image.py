from io import BytesIO
from pathlib import Path
from typing import Union

from .decorators import check_pil_importable
from .errors import InvalidFormat
from .utils import VALID_FORMATS, is_path

try:
    from PIL import Image
except ImportError:
    pass


class HCImage():
    __slots__ = ['url', 'error_code', 'response', 'format',
                 'byteio', 'get_bytes', 'get_buffer']

    def __init__(self, url: str, error_code: int,
                 response: bytes, **kwargs):
        """Initialise an instance of the HCImage class

        :param url: the URL of the image
        :type url: str
        :param error_code: the error code associated with the HTTP GET request
        :type error_code: int
        :param response: the response from the HTTP GET request
        :type response: bytes
        :param format: lock the image format to a certain format,
            defaults to "jpeg"
        :type format: str, optional
        """
        self.url = url
        self.error_code = error_code
        self.response = response
        self.format = kwargs.get("format", None)
        self.byteio = BytesIO(response) if response else None
        self.get_bytes = self.byteio.getvalue() if self.byteio else None
        self.get_buffer = self.byteio.getbuffer() if self.byteio else None

    def __str__(self):
        return self.url

    def __eq__(self, other: object) -> bool:
        try:
            return self.url == other.url
        except (AttributeError, TypeError):
            return False

    def __hash__(self) -> int:
        return hash(self._url)

    @check_pil_importable
    def save(self, fp: Union[str, Path, bytes],
             fileformat: str = None, quality: int = 100) -> None:
        """Save an image to disc or bytes

        :param fp: filename, pathlib.Path, or file object
        :type fp: Union[str, Path, bytes]
        :param fileformat: "jpeg" or "jpg", "png", "webp" , defaults to "jpeg"
        :type fileformat: str, optional
        :param quality: value between 1 and 100 inclusive, defaults to 100
        :type quality: int, optional
        """
        if not 1 <= quality <= 100:
            raise ValueError("quality must be between 1 and 100")
        elif not is_path(fp):
            raise ValueError("fp must be a filename, pathlib.Path, or file object")

        if self.format:
            fileformat = self.format.upper() if self.format.lower() != "jpg" else "JPEG"
        elif fileformat.lower() == "jpg":
            fileformat = "JPEG"
        elif fileformat.lower() not in VALID_FORMATS:
            raise InvalidFormat(fileformat)
        else:
            fileformat = fileformat.upper()

        image = Image.open(self.byteio, formats=["JPEG"])
        image.save(fp, fileformat, quality=quality)

    @check_pil_importable
    def show(self):
        image = Image.open(self.byteio)
        image.show()
