#!/usr/bin/env python3

"""
make_multiplier type-annotated function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier
    """
    def multiplier_function(number: float):
        return number * multiplier
    return multiplier_function
