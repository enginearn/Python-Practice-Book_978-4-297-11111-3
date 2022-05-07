# threadPoolExecutorはExecutorの具象クラス
from asyncio import futures
from concurrent.futures import (
    ThreadPoolExecutor,
    Future,
    as_completed
)
from re import A
from unicodedata import name

# 非同期を行いたい処理
def func():
    return 1

# 非同期を行い処理をsubmit()に渡す
future = ThreadPoolExecutor().submit(func)
print(isinstance(future, Future))

# 非同期で実行スタ処理の戻り値を取得
print(future.result())

# 現在の状態を確認する
print(future.done())

print(future.running())

print(future.cancelled())

# 対象URL一覧
urls = [
    "https://twitter.com",
    "https://facebook.com",
    'https://instagram.com'
]

from hashlib import md5
from pathlib import Path
from urllib import request

# URLをダウンロードする
def download(url):
    req = request.Request(url)

    # ファイル名に / などが含まれないようにする
    name = md5(url.encode("utf-8")).hexdigest()
    file_path = "./" + name

    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path

print(download(urls[0]))

# 逐次処理の実装
import time

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper

@elapsed_time
def get_sequential():
    for url in urls:
        print(download(url))

print(get_sequential())

# マルチスレッドでの実装
from concurrent.futures import(
    ThreadPoolExecutor,
    as_completed
)

@elapsed_time
def get_multi_thread():
    # max_workersのデフォルトはコア×5
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download, url) for url in urls]

    for future in as_completed(futures):
        # 完了したものから取得できる
        print(f"マルチスレッド: {future.result()}")

get_multi_thread()

from concurrent.futures import(
    ThreadPoolExecutor,
    wait
)

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        # self.count = self.count + 1
        self.count += 1

def count_up(counter):
    # 1,000,000
    for _ in range(1000000):
        counter.increment()

counter = Counter()

threads = 2

with ThreadPoolExecutor() as e:
    # ２つのスレッドを用意し、それぞれでcount_upを呼び出す
    futures = [e.submit(count_up, counter) for _ in range(threads)]

    done, not_done = wait(futures)

# 数値をカンマ区切りで表示
print(f"スレッドアンセーフ: {counter.count=:,}")

# スレッドセーフな実装
import threading

class ThreadSafeCounter:
    # ロックを用意する
    lock = threading.Lock()
    
    def __init__(self) -> None:
        self.count = 0
    
    def increment(self):
        with self.lock:
            # 排他制御したい一連の処理をこのブロック内に書く
            self.count = self. count + 1

counter = ThreadSafeCounter()
threads = 2

with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter) for _ in range(threads)]
    done, not_done = wait(futures)

print(f"スレッドセーフ: {counter.count=:,}")
