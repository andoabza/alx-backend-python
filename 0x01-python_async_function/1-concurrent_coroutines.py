#!/usr/bin/env python3
"""list of delay sec"""
wait_random = __import__('0-basic_async_syntax').wait_random


lock = asyncio.Lock()
delays = []

async def wait_n(n, max_delay):
   global delays
   delays = []
   tasks = []
   for _ in range(n):
       task = asyncio.create_task(wait_random(max_delay))
       tasks.append(task)
   await asyncio.gather(*tasks)
   return sorted(delays)
