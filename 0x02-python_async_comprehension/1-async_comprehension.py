#!/usr/bin/env python3
"""Defining a Async Comprehension"""
import random
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """This method returns 10 random numbers"""
    return [i async for i in async_generator()]
