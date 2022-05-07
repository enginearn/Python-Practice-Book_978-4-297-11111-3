def has_book(items):
    for item in items:
        if "book" in item:
            print("for: Found!")
            break # ループを抜ける
        else:
            print("for: Not Found...")

has_book(["note"])
has_book(["note", "book"])


def has_book(items):
    # pop()はリストの内容を変更するのでコピーを作る
    copied = items.copy()

    while copied:
        item = copied.pop()

        if "book" in item:
            print("while: Found!")
            break
        else:
            print("while: Not Found...")

has_book(["note"])
has_book(["note", "book"])


def list_books_for(items):
    for item in items:
        if "book" not in item:
            continue

        print(item)

list_books_for(["note", "book", "notebook", "sketchbook"])


def list_books_while(items):
    copied = items.copy()
    
    while copied:
        item = copied.pop(0)

        if "book" not in item:
            continue

        print(item)

list_books_while(["note", "book", "notebook", "sketchbook"])

import random

def lottery(goods):

    # :=を使わない場合、変数itemでrandomの結果を一度代入する必要がある
    # item = random.choice(goods)
    # if item

    if item := random.choice(goods):
        return item

    else:
        return "Miss..."

books = ["notebook", "sketchbook", None]

print("================================")
print(lottery(books))