#!/usr/bin/env python3

from typing import Union

"""
to_kv type-annotated function
"""


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments and returns a tuple. 
    The first element of the tuple is the string k. 
    The second element is the square of the int/float 
    v and should be annotated as a float.
    """
    tup: tuple[str, float] = (k, v*v)
    return tup