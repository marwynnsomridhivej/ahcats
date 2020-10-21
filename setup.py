from setuptools import setup, find_packages

with open("./README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ahcats",
    version="1.0.0-alpha.2",
    description="An async ready wrapper for the HTTP Cat API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marwynn Somridhivej",
    author_email="msomridhivej329@gmail.com",
    url="https://github.com/marwynnsomridhivej/ahcats",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='wrapper, api, cat, http, async',
    package_dir={"": "ahcats"},
    packages=find_packages(where='ahcats'),
    python_requires=">=3.5.3, <4",
    install_requires=['aiohttp', 'asyncstdlib'],
    extras_require={
        "pil": ['pillow'],
        "test": ['pytest-asyncio', 'pytest']
    },
)
