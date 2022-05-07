def f(x):
    # 現在のローカルスコープの内容を表示
    print(locals())
    value = "book"

    # 変数valueの定義後ローカルスコープの内容を表示
    print(locals())


print(f("python"))
print(locals())