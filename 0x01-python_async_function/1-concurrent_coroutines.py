#!/usr/bin/env python3
"""list of delay sec"""
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """result of float"""
    result = []
    for i in range(n):
        delay = await wait_random(n * max_delay)
        result.append(delay)
    return result
