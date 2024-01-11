#!/usr/bin/env python3
"""mixed list sum"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    sum = float(0)
    for x in mxd_lst:
        sum += x
    return sum
