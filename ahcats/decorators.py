import functools

from .errors import MissingDependency


def check_pil_importable(func: callable):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        """Decorator interface to check if the Pillow module can be
        imported

        :param func: the function to decorate
        :type func: callable
        :raises MissingDependency: error raised if Pillow cannot be imported
        :return: the return value of the function
        :rtype: HCImage
        """
        try:
            import PIL
        except ImportError:
            raise MissingDependency("PIL")
        else:
            return func(*args, **kwargs)
    return decorator
