import os
import time
import sys

from concurrent.futures import(
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed
)

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, b + a
    else:
        return a

print(f"fibonacci: {fibonacci(1000000)}")

# 実行時間計測デコレーター
def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        
        return v
    return wrapper

# 逐次処理の実装
# @elapsed_time
# def get_sequential(nums):
#     for num in nums:
#         print(f"逐次処理: {fibonacci(num)}")

# m = 1000000

# def main():
#     # m = int(sys.argv[1])
#     nums = [m] * os.cpu_count()
#     get_sequential(nums)


# マルチプロセスでの実装
# @elapsed_time
# def get_multi_process(nums):
#     with ProcessPoolExecutor() as e:
#         futures = [e.submit(fibonacci, num) for num in nums]

#         for future in as_completed(futures):
#             print(f"マルチプロセス: {future.result()}")

# l = 1000000

# def main():
#     nums = [l] * os.cpu_count()
#     get_multi_process(nums)


# マルチスレッドでの実装
@elapsed_time
def get_multi_thread(nums):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())

o = 1000000

def main():
    nums = [o] * os.cpu_count()
    get_multi_thread(nums)

if __name__ == "__main__":
    main()