#!/usr/bin/env python3

from typing import Iterable, Tuple, List, Sequence

"""
Annotate the below function’s parameters and return values with the appropriate types
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier
    """

    return [(i, len(i)) for i in lst]
