import string
import random


def id_generator(size=10, chars=None):
    """
    Generate a random string with 10 characters.
    This function have more explain here:

    http://stackoverflow.com/questions/2257441/
    random-string-generation-with-upper-case-letters-and-digits-in-python

    very pythonic way.
    """
    if not chars:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
