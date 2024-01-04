#!/usr/bin/env python3

from typing import List

"""
sum_list type-annotated function
"""


def sum_list(input_list: List[float]) -> float:
    """
    takes a list input_list of floats as argument and returns their sum as a float
    """
    sum: float = 0
    for item in input_list:
        sum = sum + item
    return sum