# 作成されるsome.txtは次項に進む前に削除する
from io import UnsupportedOperation

# ファイルを書き込みモードでオープンする
f = open("some.txt", "w")

try:
    # 書き込みモードなので読み込めない
    f.read()

except UnsupportedOperation as e:
    print(f"例外が発生しました: {e}")

finally:
    print("ファイルをクローズします")
    f.close()


# ファイルを読み取りモードでオープンする
f = open("some.txt", "r")

try:
    print(f.read())

finally:
    print("ファイルをクローズします")
    f.close()


# ファイルを読み取りモードでオープンする
f = open("some.txt", "w")

try:
    # 読み取りモードなので書き込めない
    f.write("egg")

finally:
    print("ファイルをクローズします")
    f.close()


f = open("some.txt", "w")

try:
    f.write("egg")
    f.close()
    f = open("some.txt", "r")
    print(f.read())
 
finally:
    print("ファイルをクローズします")
    f.close()