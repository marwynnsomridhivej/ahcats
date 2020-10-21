import asyncio
import os

from ahcats import Client, utils

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass
finally:
    loop = asyncio.get_event_loop()


CODES = [
    100, 101, 200, 201, 202, 204,
    206, 207, 300, 301, 302, 303,
    304, 305, 307, 400, 401, 402,
    403, 404, 405, 406, 408, 409,
    410, 411, 412, 413, 414, 418,
    420, 421, 422, 423, 424, 425,
    426, 429, 431, 444, 450, 451,
    499, 500, 501, 502, 503, 504,
    506, 507, 508, 509, 510, 511,
    599,
]


async def test(url: str, error_code: int, image_format: str):
    image = await ahclient.get_image(error_code)
    print(image.url, image.error_code)
    assert image.url == url
    assert image.error_code == error_code
    image.save(f"./images/{error_code}.{image_format.replace('jpeg 2000', 'jp2')}", fileformat=image_format)

ahclient = Client(default_format="jpg")
if not os.path.exists("./images"):
    os.makedirs("./images")
for formats in utils.VALID_FORMATS:
    for code in CODES:
        loop.run_until_complete(test(f"https://http.cat/{code}.jpg", code, formats))
os.remove("./images")