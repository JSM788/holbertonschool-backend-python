#!/usr/bin/env python3
"""Defining a Async Comprehension"""
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This method returns 10 random numbers"""
    return [i async for i in async_generator()]
