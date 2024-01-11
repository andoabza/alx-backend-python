#!/usr/bin/env python3
"""floats sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of the list"""
    sum = 0
    for x in input_list:
        sum += x
    return sum
