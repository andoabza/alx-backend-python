#!/usr/bin/env python3
"""callable"""
from typing import Callable
import functools
import operator


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function that multiplies a float by multiplier"""
    return functools.partial(operator.mul, multiplier)
