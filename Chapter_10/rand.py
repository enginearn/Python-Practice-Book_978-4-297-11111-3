from concurrent.futures import(
    ProcessPoolExecutor,
    as_completed
)

import numpy as np

def use_numpy_random():
    # 乱数生成器を初期化する場合は、この行を実行する
    np.random.seed()
    return np.random.random()

def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random) for _ in range(3)]
        
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()