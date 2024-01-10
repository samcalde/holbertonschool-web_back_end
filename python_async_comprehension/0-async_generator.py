#!/usr/bin/env python3

"""
Async comprehension
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator:
    """
    yield a random number between 0 and 10 (x10)
    """
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
