#!/usr/bin/env python3
"""list of delay sec"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import time


async def wait_n(n: int, max_delay: int) -> float:
    """return list of floats"""
    result = []
    for i in range(n):
        delay = await wait_random(max_delay)
        result.append(delay)
    return sorted(result)
