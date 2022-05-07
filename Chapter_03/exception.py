def get_book(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        return print(items[index])

    except IndexError:
        return print("範囲外です！")

get_book(2)


def get_book(index):
    items = ["note", "notebook", "sketchbok"]

    try:
        return items[index]

    except (IndexError, TypeError) as e:
        print(f"例外が発生しました: {e}")
        return "範囲外です！"

get_book(3)
get_book("3")


def get_book(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        return items[index]
    
    except IndexError:
        print("IndexErrorが発生しました！")
        return "範囲外です"
    
    except TypeError:
        print("TypeErrorが発生しました！")
        return "範囲外です"

get_book(3)
get_book("3")


def get_book(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        return items[index]
    
    except TypeError: # IndexErrorは捕捉しない
        print(f"TypeErrorが発生しました！")
        return "範囲外です"


def get_book_wrapper(index):
    try:
        # IndexErrorはそのまま創出されてくる
        return get_book(index)

    except IndexError:
        print(f"IndexErrorが発生しました！")
        return "範囲外です"

get_book_wrapper(3)


def get_book_upper(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        book = str(items[index])
        return print(book.upper())

    except (IndexError, TypeError) as e:
        print(f"例外が発生しました: {e}")

get_book_upper(2)


def get_book_upper(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        book = str(items[index])

    except (IndexError, TypeError) as e:
        print(f"例外が発生しました: {e}")

    else:
        return print(book.upper())

get_book_upper(3)