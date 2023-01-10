#!/usr/bin/env python3

[2;2R[3;1R[>77;30502;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
