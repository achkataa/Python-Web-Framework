import asyncio
import time
from time import sleep


async def worker1():
    return 'bread'


async def worker2():
    return 'cheese'


async def worker3():
    return 'bacon'


async def main():
    start = time.time()
    sandwich_ingredients =await asyncio.gather(
        worker1(),
        worker2(),
        worker3()
    )
    end = time.time()
    print(end - start)
    print(sandwich_ingredients)


asyncio.run(main())