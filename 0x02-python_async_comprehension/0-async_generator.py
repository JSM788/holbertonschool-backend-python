#!/usr/bin/env python3
"""Defining a coroutine that takes no arguments"""
import asyncio
import random


async def async_generator():
    """This coroutine returns random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
