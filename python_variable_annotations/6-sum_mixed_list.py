#!/usr/bin/env python3

"""
sum_mixed_list type-annotated function
"""


from typing import Union, List


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    takes a list input_list of integers and floats and returns their sum as a float
    """
    return sum(input_list)
