from typing import List


class AHCatsException(ValueError):
    """The base exception class for ahcats modules

    :param message: the message to be printed in traceback
    :type message: str
    """
    __slots__ = ['message']

    def __init__(self, message: str) -> None:
        super(AHCatsException, self).__init__(message)
        self.message = message


class HTTPError(AHCatsException):
    """This exception is raised when aiohttp returns a status code
    that is not in the 200s

    :param url: the url that was requested
    :type url: str
    :param error_code: the error code returned from the HTTP GET request
    :type error_code: int
    """
    __slots__ = ['url', 'error_code']

    def __init__(self, url: str, error_code: int) -> None:
        super().__init__(f"Request to {url} raised HTTP Error {str(error_code)}")
        self.url = url
        self.error_code = error_code


class InvalidFormat(AHCatsException):
    """This exception is raised whenever the user specifies
    and invalid file format when saving an image

    :param fileformat: the fileformat supplies
    :type fileformat: str
    """
    __slots__ = ['fileformat']

    def __init__(self, fileformat: str) -> None:
        super().__init__(f"The format \"{fileformat}\" is not a "
                         "supported or valid image format")
        self.fileformat = fileformat


class MissingDependency(AHCatsException):
    """This exception is raised whenever the user attempts
    to call a function when some or all of the required dependencies
    are not installed

    :param dependency: the dependencies that are missing
    :type dependency: List[str]
    """
    __slots__ = ['dependencies']

    def __init__(self, dependencies: List[str]) -> None:
        super().__init__("You are missing the dependencies "
                         f"{', '.join(dependencies)}, which this function requires")
        self.dependencies = dependencies
