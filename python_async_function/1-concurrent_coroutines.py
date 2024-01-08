#!/usr/bin/env python3

"""
Async coroutine
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    spawn wait_random n times with the specified max_delay
    """
    task = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*task)
    return results
