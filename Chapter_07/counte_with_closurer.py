def counter():
    count = 0
    
    def _increment():
        nonlocal count
        count += 1
        return count
    
    return _increment

counter1 = counter()
print(counter1)
print(counter1())