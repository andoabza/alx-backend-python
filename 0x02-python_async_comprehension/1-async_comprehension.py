#!/usr/bin/env python3
"""async comprehension"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """async comprehension"""
    return [i async for i in async_generator()]
