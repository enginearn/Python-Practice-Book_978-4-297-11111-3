# yieldを含む関数はジェネレーターになる
# def inf(n):
#     while True:
#         yield n

# for i in inf(3):
#     print(i)

from ast import Return
from email import iterators
from inspect import ismethoddescriptor
from msilib.schema import InstallUISequence
from multiprocessing.sharedctypes import Value


def gen_function(n):
    print("start")

    while n:
        print(f"yeild: {n}")

        # ここで一時中断される
        yield n

        n -= 1

# 戻り値はジェネレーターイテレーター
gen = gen_function(2)
print(gen)

# 組み込み関数next()に渡すと __next__()が呼ばれる
print(next(gen))
print(next(gen))
# print(next(gen))

def gen_function(n):
    while n:
        yield n
        n -= 1

# for文での利用
for i in gen_function(3):
    print(f"for文: {i}")

# 内包表記での利用
print(f"内包表記: {[i for i in gen_function(5)]}")

# イテラブルを受け取る関数に渡す
print(f"{max(gen_function(100))}")

x = list(range(1, 6))

# これはリスト内包表記
listcomp = [i ** 2 for i in x]
print(f"{listcomp}")

# これはジェネレーター式
gen = (i ** 2 for i in x)
print(gen)
print(list(gen))

def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v

iterables = ("Python", "Practice", "Book")

print(list(chain(iterables)))

# yield fromで書き直した場合
def chain(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)

print(list(chain(iterables)))

def  gen(n):
    while n:
        yield n

        n -= 1

# zip()にリストとジェネレーターを同時に渡す
x = list(range(1, 6))

print(f"{[i for i in zip(x, gen(5))]}")

# filter()にジェネレーターを渡す
odd = filter(lambda v: v % 2 == 1, gen(5))

print(f"{[i for i in odd]}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"{[i for i in zip(list1, list2)]}")
print(f"{[i for i in zip([1, 2, 3], [4, 5, 6])]}")

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)

print(f"{[i for i in zip(names, ages)]}")

# ファイルの中身を1行ずつ読み込む
def reader(src):
    with open(src, encoding="utf-8_sig") as f:
        for line in f:
            yield line

# 行単位で実行する変換処理
def convert(line):
    return line.upper()

# 読み込み → 変換 → 書き込みを1行ずつ行う
def writer(dest, reader):
    with open(dest, "w", encoding="utf-8") as f:
        for line in reader:
            f.write(convert(line))

# reader()には存在するファイルのパスを渡す
writer("dest.txt", reader("src.txt"))

from functools import lru_cache, wraps
from time import sleep

# 最近の呼び出し最大100回までキャッシュ
@lru_cache(maxsize=100)
def heavy_function(n):
    sleep(1)

    return n + 1

print(f"{heavy_function(2)}")
print(f"{heavy_function(99)}")

from dataclasses import dataclass

@dataclass(frozen=True)
class Fruit:
    
    # 型ヒントをつけて属性を定義
    name: str

    # 初期値も指定
    price: int = 0

# __init__()や__repr()が自動で追加されている
apple = Fruit(name="apple", price=128)
print(apple)

# frozen=Trueとしたので読み取り専用
# apple.price = 256

# デコレートしたい関数を受け取る
def deco1(f):
    print("deco1 called")
    
    def wrapper():
        print("before exec")

        # 元の関数を実行
        v = f()

        print("after exec")
        return v
    return wrapper

# デコレーターは関数定義時に実行される
@deco1
def func():
    print("exec")
    return print(f"wrapperの戻り値: {1}")

# deco1(func)の結果に置き換わっている
print(func.__name__)

# func()の呼び出しはwrapper()の呼び出しになる
func()

def deco2(f):
    # 新しい関数が引数を受け取る
    def wrapper(*args, **kwargs):
        print("before exec")

        # 引数を渡してもとの関数を実行
        v = f(*args, **kwargs)
        print("after exec")

        return v
    return wrapper

@deco2
def func(x, y):
    print("exec")
    return x, y

print(func(1, 2))

# 引数zを受け取る
def deco3(z):
    # deco2()と同等
    def _deco3(f):
        def wrapper(*args, **kwargs):
            # ここでzを参照できる
            print("before exec", z)

            v = f(*args, **kwargs)
            print("after exec", z)
            return v
        return wrapper
    
    # _deco3を返す
    return _deco3

# deco3(z=3)の戻り値がデコレーターの実態
# つまりfunc = deco3(z=3)(func)と同等
@deco3(z=3)
def func(x, y):
    print("exec")
    return x, y

print(func(1, 2))
print(func(10, {"a": 1, "あいうえおかきくけこ": "ABCDEFG"}))

# 複数のデコレーターを利用
@deco3(z=3)
@deco3(z=4)
def func(x, y):
    print("exec")
    return x, y

# @deco3(z=4)が適用された結果に
# @deco3(z=3)が適用される
print(func(1, 2))

from functools import wraps

def deco4(f):
    # もとの関数を引数に取るデコレーター
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("before exec")

        v = f(*args, **kwargs)
        print("after exec")
        return v
    return wrapper

@deco4
def func():
    """funcです"""
    print("exec")

print(func.__name__)
print(func.__doc__)

import time

def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - start}")
        return v
    return wrapper

# 0からn-1までの総和を計算する関数
@elapsed_time
def func(n):
    return sum(i for i in range(n))

# func()の実行結果を表示
# f-stringで数値のカンマ(,)区切りを指定
print(f"{func(1000000)=:,}")
print(f"{func(10000000)=:,}")

# 第二引数で書き込みモードを指定
with open("some.txt", "w") as f:
    f.write("Python")

print(f.closed)

# try:
#     f = open("some.txt", "w")
#     f.read()

# finally:
#     f.close()

# このクラスのインスタンスがコンテテキストマネージャー
class ContexManager:
    # 前処理を実装
    def __enter__(self):
        print("__enter__ was called")

    # 後処理を実装
    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ was called")
        print(f"{exc_type=}")
        print(f"{exc_value=}")
        print(f"{traceback=}")

# withブロックが正常終了の場合は
# __exit__()の引数はすべてNone
with ContexManager():
    print("inside the block")

# withブロック内で例外が発生した場合は
# その情報が__exit__()に渡される
# with ContexManager():
#     1 / 0

class ContextManager:
    # 戻り値がasキーワードに渡される
    def __enter__(self):
        return 1

    def __exit__(self, exc_type, exc_value, traceback):
        pass

with ContextManager() as f:
    print(f)

with ContextManager():
    pass

class Point:
    def __init__(self, **kwargs):
        self.value = kwargs
    def __enter__(self):
        print("__enter__ was called")
        
        # as節で渡される
        return self.value

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ was called")
        print(self.value)

with Point(x = 1, y = 2) as p:
    print(p)
    p['z'] = 3

from contextlib import contextmanager

@contextmanager
def point(**kwargs):
    print("__enter__ was called")
    Value = kwargs

    try:
        # yield式より上が前処理
        # valueがsaキーワードに渡される
        yield Value
        # yield式より下が後処理
    
    except Exception as e:
        # エラー時はこちらも呼ばれる
        print(e)
        raise
    finally:
        print("__exit__ was called")
        print(Value)

with point(x = 1, y = 2) as p:
    print(p)
    p["z"] = 3

print(dir(property()))
print(type(property()))

class A:
    def f(self):
        pass

# でスクリプタが持つメソッドが定義されている
print(dir(A.f))
# メソッドはfunctionクラス
print(type(A.f))

# __set__()を持つクラスはデータデスクリプタ
class TextField:
    def __set_name__(self, owner, name):
        print(f"__set_name__ was called")
        print(f"{owner=}, {name=}")

        self.name = name

    def __set__(self, instance, value):
        print("__set__ was called")
        if not isinstance(value, str):
            raise AttributeError("must be str...")

        # ドット起法ではなく属性辞書を使って格納
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print("__get__ was called")
        return instance.__dict__[self.name]

# データデスクリプタを使うBookクラス
class Book:
    title = TextField()

book = Book()

# 代入時には__set__()が呼ばれる
book.title = "Python Practice Book"

# 取得時には__get__()が呼ばれる
print(book.title)

# 別のインスタンスを作成して代入
notebook = Book()
notebook.title = "NoteBook"

# それぞれのデータを保持している
print(book.title)
print(notebook.title)

# タイトルは文字列のみ
# book.title = 123
# print(book.title)

# __get__()のみの非データデスクリプタ
class TextField:
    def __init__(self, value):
        if not isinstance(value, str):
            raise AttributeError("must be str...")
        self.value = value

    def __set_name__(self, owner, name):
        print(f"__set_name__ was called")
        print(f"{owner=}, {name=}")
        self.name = name

    def __get__(self, instance, owner):
        print("__get__ was called")
        return self.value

class Book:
    title = TextField("Python Practice Book")

book = Book()
print(book.title)

book.title = "Just Book"
print(book.title)

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if not instance:
            # クラス変数としてアクセスされた時の処理
            return self

            # self.funcは関数なので明示的にインスタンスを渡す
        v = self.func(instance)
        instance.__dict__[self.name] = v

        return v

TAX_RATE = 1.10

class Book:
    def __init__(self, raw_price):
        self.raw_price = raw_price

    @LazyProperty
    def price(self):
        print("calculate the price")
        return int(self.raw_price * TAX_RATE)

book = Book(1979)
print(book.price)
print(book.price)
print(Book.price)