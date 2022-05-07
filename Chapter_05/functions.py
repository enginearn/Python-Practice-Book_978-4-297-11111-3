def print_page():
    print("no content")

print_page()

def print_page(content):
    print(content)

print_page("my contents")

def print_title(printer, title):
    print("@@@@@")

    # 引数printerは関数オブジェクト
    printer(title.upper())

    print("@@@@@")

print_title(print_page, "python practice book")

def increment(page_num):
    return page_num + 1

next_page = increment(1)

print(next_page)
print(increment(increment(next_page)))

def increment(page_num, last):
    next_page = page_num + 1
    
    if next_page <= last:
        return next_page

    raise ValueError("invalid arguments")

print(increment(1, 3))
# print(increment(3, 3))

def no_value():
    return

print(no_value())

def no_return():
    pass

print(no_return())

def increment(page_num, last):
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    raise ValueError("Invalid arguents")

print(increment(9, 10))

from datetime import datetime
from importlib.resources import contents

def print_page(content, timestamp=datetime.now()):
    print(f"content: {content}, timestamp: {timestamp}")

print_page("my content1")

def print_page2(content, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    print(f"content: {content}, timestamp: {timestamp}")

print_page("my content2")

def print_pages(content, *args):
    print(content)
    for more in args:
        print(f"more: {more}")
    # print(f"more: {more}" for more in args)

print_pages("my content1", "content2", "content3", "content4", "content5")

def print_pages(content, **kwargs):
    print(content)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_pages("my content", published="2022", author="John Smith")

def print_pages(*args, **kwargs):
    for content in args:
        print(content)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_pages("content1", "content2", "content3",
            published=2022, author="John Smith")

def increment(page_num, last, *, ignore_error=False):
    """次のページ番号を返す

    :param page_num: もとのページ番号
    :type page_num: int
    :param last 最終ページ
    :type last: int
    :param ignore_error: Trueの場合、ページのオーバーで例外を送出しない
    :type ignore_error: bool
    :rtype: int
    """
    next_page = page_num + 1
    
    if next_page <= last:
        return next_page
    
    if ignore_error:
        return None
    
    raise ValueError("Invalid arguments")

increment(2, 2, ignore_error=True)
# increment(2, 2, True)

def add(x, y, /, z):
    return print(x + y + z)

add(1, 2, 3)
add(1, 2, z = 3)

def print_page(one, two, three):
    print(one)
    print(two)
    print(three)

contents = ["my content", "content2", "content3"]

print_page(*contents)

def print_page(content, published, author):
    print(content)
    print(f"published: {published}")
    print(f"author: {author}")

footer = {"published": 2022, "author": "John Smith"}

print_page("my content", **footer)

increment = lambda num : num + 1

print(increment(1))

nums = ["one", "two", "three", "four", "five"]

filtered_result = filter(lambda x : len(x) == 3, nums)

print(list(filtered_result))
print(list(filtered_result)[:])

from typing import Optional

def increment(
    page_num: int,
    last: int,
    *,
    ignore_error: bool = False) -> Optional[int]:

    next_page = page_num + 1
    if next_page <= last:
        return next_page
    
    if ignore_error:
        return None
    
    raise ValueError("Invalid arguments")

print(increment.__annotations__)
print(increment(1, 3, ignore_error=1))

def decrement(page_num: int) -> int:
    prev_page: int # 型情報を付けて変数を宣言
    prev_page = page_num - 1
    return prev_page

print(decrement(2))
print(decrement(2.0))