#!/usr/bin/env python3
"""to kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    tuple1 = ('k',)
    tuple2 = (k, v * v)
    return tuple2
