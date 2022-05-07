def first_item(items):
    if items:
        return items[0]

    else:
        return None

content = first_item(["book"])

print("リストの中身: ", content)

content = first_item([])

print(f"リストの中身: {content}")