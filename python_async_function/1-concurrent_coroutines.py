#!/usr/bin/env python3

"""
Async coroutine
"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    finished_tasks_list = []
    for task in asyncio.as_completed(tasks):
        time = await task
        finished_tasks_list.append(time)
    return finished_tasks_list
