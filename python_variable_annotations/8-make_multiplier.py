#!/usr/bin/env python3

from typing import Callable

"""
make_multiplier type-annotated function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier
    """
    def multiplier_function(number: float):
        return number * multiplier
    return multiplier_function
