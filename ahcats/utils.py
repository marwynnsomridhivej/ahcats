from io import BytesIO
from pathlib import Path
from typing import Any


VALID_FORMATS = [
    'bmp',
    'dib',
    'eps',
    'gif',
    'icns',
    'ico',
    'im',
    'jpeg',
    'jpeg 2000',
    'msp',
    'pcx',
    'png',
    'ppm',
    'sgi',
    'tga',
    'tiff',
    'webp',
    'xbm',
]


def is_path(path: Any) -> bool:
    return isinstance(path, (str, Path, BytesIO))
