#!/usr/bin/env python3
"""coroutine that will loop 10 time"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
