#!/usr/bin/env python3
"""measure time"""
import time
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n"""
    start = time.time()
    wait_random(n, max_delay)
    return (time.time() - start) / 5
