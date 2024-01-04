#!/usr/bin/env python3

"""
Annotate the function parameters, return values with the appropriate types
"""


from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier
    """

    return [(i, len(i)) for i in lst]
