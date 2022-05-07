from ast import Num
from re import X


class Page: # クラスの定義
    def __init__(self, num, content):
        self.num = num # ページ番号
        self.content = content # ページの内容
    
    def output(self):
        return f"{self.content}"

print(Page)

# インスタンス化
title_page = Page(0, "Python Practice Book")
print(type(title_page))

# Pageクラスのインスタンスか確認
print(isinstance(title_page, Page))

# インスタンスが持つ属性を確認
print(dir(title_page))

# インスタンスメソッドの呼び出し
print(title_page.output())

# インスタンスメソッド（classで定義したメソッド（関数））と（単独の）関数は同じで、functionクラスのインスタンスとして実現される
class Class:
    # インスタンスメソッドを定義
    def some_method(self):
        print("method!")

# 同じ引数の関数を定義
def some_function(self):
    print("function!")

# インスタンス化
create_instance = Class()
print(f"インスタンスメソッド: {create_instance.some_method()}")
print(f"{type(create_instance.some_method)}")

# 関数呼び出し
print(f"{some_function('self')}")


# 関数はfunctionクラスのインスタンス
print(f"{type(some_function)}, ファンクション: {some_function(0)}")

# インスタンスメソッドもfunctionクラスのインスタンス
print(f"{type(Class.some_method)}, インスタンスメソッド: {create_instance.some_method()}")

Class.some_function = some_function

create_instance.some_function()

# title_pageに新しいインスタンス変数sectionを定義
title_page.section = 0
print(title_page.section)

# 別のインスタンス(first_page)を作成
first_page = Page(1, "first page")
# 先ほどのインスタンス変数sectionは存在しないのでAttributeError
# print(first_page.section)

class Page:
    def __init__(self, num, content, section=None):
        self.num = num
        self.content = content
        self.section = section
    
    def output(self):
        return f"{self.content}"

# インスタンスを作成
title_page = Page(0, "Python Practice Book")

# sctionはNone
title_page.section
print(title_page.output())

# sectionを指定して別のインスタンスを作成
first_page = Page(1, "first page", 1)
print(first_page.section)
print(first_page.output())

class Class:
    # コンストラクタ
    def __new__(cls, *args):
        print(f"{cls=}")
        print(f"new: {args}")
        # インスタンスを作成して返す
        return super().__new__(cls)

    # イニシャライザ
    def __init__(self, *args):
        # インスタンスの初期化はイニシャライザの役割
        print(f"init: {args}")


# インスタンス化
cls = Class(1, 2, 3)

class Evil:
    def __new__(cls, *args):
        return 1

# Evilクラスをインスタンス化
evil = Evil()
print(evil)
isinstance(evil, Evil)
print(type(evil))

# class Evilを継承してMyClassを作成、print_classメソッドを追加
class MyClass(Evil):
    def print_class(self):
        print("MyClass")

# インスタンス化
my = MyClass()

# AttributeError
# my.print_class()

class Book:
    def __init__(self, raw_price):
        if raw_price < 0:
            raise ValueError("price must be positive!")
        
        self.raw_price = raw_price
        self._discounts = 0
    
    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if value < 0 or 100 < value:
            raise ValueError(
                "discounts must be between 0 and 100"
            )

        self._discounts = value

    @property
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)

# インスタンス化
book = Book(2000)

# 割引率初期値は0
print(f"割引率: {book.discounts}%")

# 割引率を20%
book.discounts = 20

print(f"割引後の価格: ¥{book.price}")

# 割引率が100を超えるとValueError
# book.discounts = 101

class Klass:
    def __init__(self, x):
        self. __x = X

kls = Klass(10)

# Klassクラスの変数__xはないと怒られる
# kls.__x

print(f"{kls._Klass__x}")

# クラス変数を持つクラスを定義
class Page:
    book_title = "Python Practice Book"

print(Page.book_title)

# クラス変数の更新
Page.book_title = "No title"
print(Page.book_title)

# クラス変数はインスタンスからも参照可能
# インスタンス化
first_page = Page()
second_page = Page()

print(f"first page: {first_page.book_title}")
print(f"second page: {second_page.book_title}")

Page.book_title = "Python Practice Book"
print(f"first page: {first_page.book_title}")
print(f"second page: {second_page.book_title}")

# インスタンスを介して代入するとクラス変数の更新ではなく、
# インスタンスだけが持つ新しいインスタンス変数になる
first_page.book_title = "(DRAFT) Python Practice Book"
print(f"{first_page.book_title}")
print(Page.book_title)

# クラス変数と同名のインスタンス変数が定義された場合、
# クラスオブジェクトの属性より先にインスタンスオブジェクトが検索されるため、
# そのインスタンスの属性からクラス変数にアクセスできない

print(f"{first_page.book_title}")

# インスタンス変数の削除
del first_page.book_title

print(f"{first_page.book_title}")

from operator import attrgetter

class Page:
    book_title = "Python Practice Book"
    
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f"{self.content}"

    # クラスメソッドの第一引数はクラスオブジェクト
    @classmethod
    def print_pages(cls, *pages):
        # クラスオブジェクトの利用
        print(cls.book_title)
        pages = list(pages)

        # ページ順に並べ替えて出力
        print([page.output() for page in sorted(pages, key=attrgetter("num"))])

# インスタンス化
first = Page(1, "first page")
second = Page(2, "second page")
third = Page(3, "third page")

# クラスメソッドの呼び出し
Page.print_pages(first, second, third)

# インスタンスからの呼び出し
first.print_pages(first, second, third)

class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    @staticmethod
    def check_blank(page):
        return bool(page.content)

page = Page(1, "")
print(Page.check_blank(page))

# クラスの継承の練習用基底クラス
class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f"{self.content}"

# メソッドのオーバーライド
class TitlePage(Page):
    def output(self):
        # 基底クラスのメソッドは自動で呼ばれないため
        # 明示的に呼び出す
        title = super().output()
        return title.upper()

title = TitlePage(0, "Python Practice Book")
print(title.output())

# 組み込み型のサブクラスを作成
class Length(float):
    def to_cm(self):
        return super().__str__() + "cm"

pencil_length = Length(16)
print(pencil_length.to_cm())

# 多重継承
class HTMLPageMixin:
    def to_html(self):
        return f"<html><body>{self.output()}</body></html>"

# 多重継承を使ったMixinの利用
class WebPage(Page, HTMLPageMixin):
    pass

page = WebPage(0, "web content")
print(page.to_html())

class A:
    def hello(self):
        print("Hello")

class B(A):
    def hello(self):
        print("Hola")
        # 基底クラスのメソッドを実行
        super().hello()

class C(A):
    def hello(self):
        print("ニーハオ")
        # 基底クラスのメソッドを実行
        super().hello()

class D(B, C):
    def hello(self):
        print("こんにちは")
        # 基底クラスのメソッドを実行
        super().hello()

d = D()

print(d.hello())
print(D.__mro__)