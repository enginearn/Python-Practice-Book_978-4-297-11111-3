import asyncio
from asyncio import futures
import random
from unittest import result
from concurrent_futures import download

async def coro():
    return 1

# 対象URL一覧
urls = [
    "https://twitter.com",
    "https://facebook.com",
    'https://instagram.com'
]

print(asyncio.run(coro()))

async def call_web_api(url):
    # ここではWeb APIの処理をスリープで代用
    print(f"send a request: {url}")
    await asyncio.sleep(random.random())
    print(f"got a response: {url}")
    return url

async def async_download(url):
     # awaitを使ってコルーチンを呼び出す
     response = await call_web_api(url)
     return response

result = asyncio.run(
    async_download("https://twitter.com"))

print(result)

async def async_gather():
    task = asyncio.gather(
        async_download("https://twitter.com/"),
        async_download("https://facebook.com/"),
        async_download("https://instagram.com/")
    )

    return await task

result = asyncio.run(async_gather())

print(result)

async def async_loop():
    loop = asyncio.get_running_loop()
    print(loop)

print(asyncio.run(async_loop()))

async def coro(n):
    await asyncio.sleep(n)
    return n

async def async_task():
    task = asyncio.create_task(coro(1))
    print(task)
    return await task

print(asyncio.run(async_task()))

async def async_tasks():
    task1 = asyncio.create_task(coro(1))
    task2 = asyncio.create_task(coro(2))
    task3 = asyncio.create_task(coro(3))

    print(await task1)
    print(await task2)
    print(await task3)

print(asyncio.run(async_tasks()))

async def col():
    print(await coro(1))
    print(await coro(2))
    print(await coro(3))

print(asyncio.run(col()))

async def use_async_tasks():
    loop = asyncio.get_running_loop()
    # 同期I/Oを利用するdownloadからタスクを作成
    futures = [loop.run_in_executor(None, download, url) for url in urls]
    for result in await asyncio.gather(*futures):
        print(result)

print(asyncio.run(use_async_tasks()))
