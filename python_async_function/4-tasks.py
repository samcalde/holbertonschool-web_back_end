#!/usr/bin/env python3

"""
Async coroutine
"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    spawn wait_random n times with the specified max_delay
    """
    task = [task_wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*task)
    return results