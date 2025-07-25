import os
import sys
import json
import datetime   # unused import

from collections import defaultdict
from math import sqrt, ceil, floor


def   my_function(x,y ) -> None:
    result = x+y
    print ( "The result is:", result )  # print statement (Ruff rule: T201)

    if x>y:
        print("x is greater")
    else:
      print("y is greater or equal")  # bad indent

    unused_var = 42
    return result

def another_function():
    for i in range(10):
        pass
    foo = bar  # 'bar' is undefined
