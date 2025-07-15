import os, sys  # Unused imports

def bad_function(a, b = 10):  # default arg with no space, no type hints
    result = a + b
    temp = "123"
    if result > 5:
        print("Result is big")
    else:
        print("Small")
    return result

def badFunctionTwo(x):  # inconsistent naming, no type hint
    x = "a string"
    x += 5  # type mismatch!
    return x

class data:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
