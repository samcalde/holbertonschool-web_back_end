#!/usr/bin/env python3

"""
sum_mixed_list type-annotated function
"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats, returns their sum as a float
    """
    sum: float = 0
    for item in mxd_lst:
        sum = sum + item
    return sum
