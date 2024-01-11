#!/usr/bin/env python3
"""rerturn floor int"""

def floor(n: float) -> float:
    """return floored n"""
    newn = int(n)
    newn1 = float(newn + 0.50)
    if n <= newn1:
        return newn
    return newn + 1
