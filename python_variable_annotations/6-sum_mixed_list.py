#!/usr/bin/env python3

from typing import Union

"""
sum_mixed_list type-annotated function
"""


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats and returns their sum as a float
    """
    sum: float = 0
    for item in mxd_lst:
        sum = sum + item
    return sum