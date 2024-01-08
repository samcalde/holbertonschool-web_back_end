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
    tasks = [task_wait_random(max_delay) for i in range(n)]
    finished_tasks_list = []
    for task in asyncio.as_completed(tasks):
        time = await task
        finished_tasks_list.append(time)
    return finished_tasks_list
