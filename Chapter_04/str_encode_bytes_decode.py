from base64 import encode


book = "Python実践入門"
print(f"{type(book)}")
print(book)

encoded = book.encode("utf-8")
print(f"{type(encoded)}")
print(encoded)

print(f"{encoded.decode('utf-8')}")