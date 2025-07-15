# bad_code.py

import math,os

def foo(x: int, y: str) -> int:
    print(   "This is bad formatted and untyped code!" )
    return x + y  # Type error: y is str

def Bar():
  a=1
  b=2
  print(  a+b  )

foo(5, "10")
Bar()
