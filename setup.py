import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ahcats",
    packages=['ahcats'],
    version="0.1.0",
    license="MIT",
    description="An async ready wrapper for the HTTP Cat API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marwynn Somridhivej",
    author_email="msomridhivej329@gmail.com",
    url="https://github.com/marwynnsomridhivej/ahcats",
    keywords=['wrapper', 'api', 'cat', 'http', 'async'],
    install_requires=['aiohttp', 'asyncstdlib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
