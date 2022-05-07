from typing import Optional

def increment(
    page_num: int,
    last: int,
    *,
    ignore_error: bool = False) -> Optional[int]:
    """
    次のページを返す
    :param page_num: 元のページ番号
    :param last: 最終ページ番号
    :param ignore_error: Trueの場合、ページのオーバーで例外を送出しない
    :return: 次のページ番号
    """

    next_page = page_num + 1
    if next_page <= last:
        return next_page

    if ignore_error:
        return None
    
    raise ValueError("Invalid arguments")

# 肩の一致していない関数呼び出し
print(increment(1, 10, ignore_error=False))