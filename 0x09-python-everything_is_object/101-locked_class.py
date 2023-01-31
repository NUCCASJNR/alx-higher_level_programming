#!/usr/bin/python3


"""LockedClass with no class or object attribute, that prevents
the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name."""


class LockedClass:

    """initializing the class"""

    __slots__ = ["first_name"]
