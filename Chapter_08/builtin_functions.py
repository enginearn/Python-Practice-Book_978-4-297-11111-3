d = {}

# 第一引数はインスタンスオブジェクト
print(isinstance(d,dict))
print(isinstance(d, object))
print(isinstance(d, (list, dict, int)))

# 第一引数はクラスオブジェクト
print(issubclass(dict, object))

# bool型はint型のサブクラス
print(issubclass(bool, (int, list, dict)))

# 辞書から値を取り出す関数
def get_value(obj, key):
    if not isinstance(obj, dict):
        raise ValueError
    return obj[key]

print(get_value({1: "A"}, 1))
print(get_value({2: "B"}, 2))
print(get_value({3: "C"}, 3))

from ast import Param
from collections import UserDict
import collections
from fileinput import filename
from multiprocessing.sharedctypes import Value
from random import random
from unicodedata import name

class MyDict(UserDict):
    pass

# 辞書のように使える
my_dict = MyDict()
my_dict["a"] = 1
print(my_dict["a"])

# dictのサブクラスではないためエラー
# print(get_value(my_dict, "a"))

from collections import abc

# MyDictクラスの基底クラスUserDictは
# 辞書として振る舞う際に必要となるメソッドを全て実装している
def get_value(obj, key):
    if not isinstance(obj, abc.Mapping):
        raise ValueError
    return obj[key]

print(get_value(my_dict, "a"))

# 関数
print(callable(isinstance))

# クラス
print(callable(Exception))

# メソッド
print(callable("".split))

class Threshold:
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, x):
        return self.threshold < x

threshold = Threshold(2)

print(threshold(3))
print(callable(threshold))
print(threshold(1))

import json
import os

# パッケージオブジェクトは必ず__path__を持つ
def is_package(moduke_or_package):
    return hasattr(moduke_or_package, "__path__")

print(f"json: {is_package(json)}")
print(f"os: {is_package(os)}")

class Mutable:
    def __init__(self, attr_map):
        # 辞書のキーを属性名にしたインスタンス変数を用意
        for k, v in attr_map.items():
            setattr(self, str(k), v)

m = Mutable({"a": 1, "b": 2})

print(f"a: {m.a}")

# m.bと同党
attr = "b"

print(f"b: {getattr(m, attr)}")

# m.aと同等
delattr(m, "a")

# m.a

text = "python"
instance_method = getattr(text, "upper")
instance_method
print(instance_method())

nums1 = list(range(1, 4))
list11 = [num for num in nums1]
print(f"list1: {list11}")
print(f"nums1: {nums1}")

nums2 = list(range(4, 8))
list22 = [num for num in nums2]
print(f"list2: {list22}")
print(f"nums2: {nums2}")

nums3 = list(range(8, 10))

zip(nums1, nums2)

print(list(zip(nums1, nums2)))
print(list(zip(nums1, nums2, nums3)))

from itertools import zip_longest
print(f"{list(zip_longest(nums1, nums2, nums3, fillvalue=0))}")

import random

x = [random.randint(1, 101) for i in range(1, 101)]
x = random.sample(range(1, 101), k=10)
y = [x.pop() for i in x]

print(f"x: {x}")
# print(f"x: {x.sort()}")
print(f"y: {y}")
print(f"y: {sorted(y)}")
print(f"y: {sorted(y,reverse=True)}")

x = ["1", "4", 3, 1, "1"]
v = ["1", "4", 3, 1, "1"]
# print(sorted(x))

print(f"{sorted(x, key=lambda v: int(v))}")

z = lambda v: int(v)
# z = [int(i) for i in v]
print(z)

x = sorted(random.sample(range(1, 6), k=5))
print(x)
print(f"{list(filter(lambda i: i > 3, x))}")

x = [1, 0, None, 2, [], "python"]
print(f"{list(filter(None, x))}")

x = list(range(1, 11))
print(list(map(lambda i: i * 10, x)))

keys = ("q", "limit", "page")
values = ("Python", 10, 2)

# 関数が受け取る引数の数と渡すイテラブルの数は一致させる
print(list(map(lambda k, v: f"{k} = {v}", keys, values)))

# join()と組み合わせてクエリ文字列を作成
print("?" + "&".join(
    map(lambda k, v: f"{k}={v}", keys, values)
    )
)

# itemgetterの挙動を確認
from operator import itemgetter

d = {"word": "Python", "count": 3}
f = itemgetter("count")

# d["count"]を返す
print(f(d))

f = itemgetter("count", "word")
# d["count", "word"]を返す
print(f(d))

# 辞書の値を使った並べ替え
counts = [
    {"word": "Python", "count": 3},
    {"word": "Practic", "count": 3},
    {"word": "Book", "count": 2},
]

print(sorted(counts, key=itemgetter('count')))

# countの値で並べ替えた後にwordの値でも並べ替えられる
print(sorted(counts, key=itemgetter("count", "word")))

# all()はすべての要素が真の場合にTrue
print(all(["Python", "Practice", "Book"]))

# 空文字が偽なので結果もFalse
print(all(["Python", "Practice", ""]))

class A:
    def __len__(self):
        return 5

a = A()

print(len(a))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p = Point(1, 2)

p
print(p)

class QueryParams:
    def __init__(self, params) -> None:
        self.params = params

    def __bool__(self):
        return bool(self.params)

query = QueryParams({})
print(bool(query))

query = QueryParams({"key": "value"})
print(bool(query))

x = list(range(10))
query = QueryParams([])
print(bool(query))

query = QueryParams(x)
print(bool(query))


class Adder:
    def __init__(self) -> None:
        self._values = []

    def add(self, x):
        self._values.append(x)

    def __call__(self):
        return sum(self._values)

adder = Adder()
adder.add(1)
print(adder())

adder.add(3)
print(adder())

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __setattr__(self, name, value) -> None:
        if name not in ("x", "y"):
            raise AttributeError("Not allowed...")
        super().__setattr__(name, value)

p = Point(1, 2)
# p.z = 3
p.x = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, name):
        if name in ("x", "y"):
            raise AttributeError("Not allowed...")

        super().__delattr__(name)

# p = Point(1, 2)

# del p.x

class Point:
    pass

p = Point()

print(p.__dict__)

# p.__dict__["x"] = 1 に変換される
p.x = 1

print(p.__dict__)

# __dict__は直接書き込み可能
p.__dict__["y"] = 2

print(p.y)

print(p.__dict__)

class Config:
    def __init__(self, filename):
        self.config = json.load(open(filename))

    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]

        raise AttributeError()

conf = Config("config.json")
print(conf.url)

class Iterable:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return iter(range(self.num))

print(f"{[val for val in Iterable(3)]}")

class Reverse:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.x.pop()
        except IndexError:
            raise StopIteration()

print(f"{[val for val in Reverse([1, 2, 3])]}")

# 1グループあたりの要素数
n = 3

s = [i for i in range(12)]

print(s)

print(f"{list(zip(*[iter(s)]*n))}")
print([iter(s)]*n)

from collections import defaultdict

class CountDict:
    def __init__(self):
        self._data = {}
        self._get_count = defaultdict(int)
        self._set_count = defaultdict(int)

    def __getitem__(self, key):
        
        # c["x"]など参照時に呼ばれる
        self._get_count[key] += 1
        return self._data[key]

    def __setitem__(self, key, value):
        # c["x"] = 1 など代入時に呼ばれる
        self._set_count[key] += 1
        self._data[key] = value

    @property
    def count(self):
        return {
            "set": list(self._set_count.items()),
            "get": list(self._get_count.items())
        }

c = CountDict()
c["x"] = 1
print(c["x"])

c["x"] = 2
c["y"] = 3

print(c.count)

class OddNumbers:
    def __contains__(self, item):
        try:
            return item % 2 == 1
        
        except:
            return False

odds = OddNumbers()

print(f"{1 in odds}")
print(f"{4 in odds}")