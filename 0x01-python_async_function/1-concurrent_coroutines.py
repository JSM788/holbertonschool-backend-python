#!/usr/bin/env python3
"""Write an async routine called wait_n that takes in 2 int arguments
n and max_delay"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """This function return the list of all the delays in order"""
    array = []
    for i in range(n):
        delay = await wait_random(max_delay)
        array.append(delay)
    result = sorted(array)
    return result
