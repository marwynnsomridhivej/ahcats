# ahcats
`ahcats` is a fully async Python wrapper for the HTTP Cats API.

Thank you for using `ahcats`! This is my first API wrapper and I appreciate your support! This wrapper is completely async.

I am only the creator of this wrapper library. The creator of the HTTP Cats API is [Rogério Vicente](https://github.com/rogeriopvl)

If you have any questions or need support with the wrapper, please join my [Discord Support Server](https://discord.gg/78XXt3Q)

# Getting Started
As with most repositories, you can install the package from the Python Package Index (PyPI). Do either one of these in your terminal:
- `pip install -U ahcats`
- `python -m pip -U install ahcats`

You can also install directly from source by entering either one of these in your terminal:
- `pip install -U git+https://github.com/marwynnsomridhivej/ahcats`
- `python -m pip install -U git+https://github.com/marwynnsomridhivej/ahcats`

## Usage
If you want more detailed examples, please check out the examples in the examples directory *(coming soon)*
```python
import ahcats
import os

ahclient = ahcats.Client(default_format="jpg")
error_code = 404
image = await ahclient.get_image(error_code)
print(image.url)

if not os.path.exists("./images"):
    os.makedirs("./images")
image.save("./images/images.jpg", fileformat="jpg")
```
**Output:**
```
http.cat/404.jpg
```
<img src="./404.jpg" alt="HTTP Cat 404 JPEG" width="30%">