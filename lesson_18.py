# async def say_hello():
#     print('hello')
#
#
# caroutine =say_hello()
# print(caroutine)


# import asyncio
#
#
# async def hello():
#     print('hello')
#     await asyncio.sleep(1)
#     print('pycharm')
#
#
# asyncio.run(hello())


# import asyncio, time
#
#
# async def coro(tag,delay):
#     t0 = time.perf_counter()
#     await asyncio.sleep(delay)
#     print(tag , 'done in '  f'{time.perf_counter() - t0:.2f}s')
#
#
# async def main():
#     await asyncio.gather(
#
#         coro('A', 8),
#         coro('S',4),
#         coro('X', 7)
#
#     )
#
# asyncio.run(main())


# import asyncio
# import time
# from time import perf_counter
#
#
# async def fake_request(name, delay):
#     await asyncio.sleep(delay)
#     return f'{name} ok'
#
# async def sequential():
#     t0 = time.perf_counter()
#     await fake_request('a',2)
#     await fake_request('b', 2)
#     print('Sequential time:', time.perf_counter()- t0)
#
#
# async def parallel():
#     t0 = time.perf_counter()
#     await asyncio.gather(
#         fake_request('a',2),
#         fake_request('b',2)
#     )
#     print('Parallel time:' , time.perf_counter()-t0)
#
#
# asyncio.run(sequential())
# asyncio.run(parallel())


import asyncio


# async def long():
#     await asyncio.sleep(2)
#     return  "hello"
#
# async def main():
#     task = asyncio.create_task(long())
#     print('doing something')
#     await  asyncio.sleep(1)
#     print('result ', await task)
#
#
# asyncio.run(main())


import asyncio
import  random


sem = asyncio.Semaphore(2)

async def download(y):
    async with sem:
        await asyncio.sleep(random.uniform(0.5,1.5))
        print(f'file {y} downloaded')

async def main():
    await asyncio.gather(*(download(i) for i in range(10)))



