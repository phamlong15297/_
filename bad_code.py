import fastapi
import sys
from typing import List, Dict
from collections import defaultdict
import pydantic
from typing import Optional

def process_data(x: int, data: list[int] = []) -> List[int]:
	print("Processing...")
	return [y * 2 for y in data]  # unnecessary list(map(...))

def build_index(data):
	index = defaultdict(list)
	for item in data:
		key = item.get("key")
		if key not in index:
			index[key] = list()
		index[key].append(item)
	return index

def unused_function():
	pass

