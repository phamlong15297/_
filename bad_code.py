from collections import defaultdict


def process_data(x: int, data: list[int] | None = None) -> list[int]:
	if data is None:
		data = []
	if data is None:
		data = []
	print("Processing...")
	return [y * 2 for y in data]  # unnecessary list(map(...))

def build_index(data):
	index = defaultdict(list)
	for item in data:
		key = item.get("key")
		if key not in index:
			index[key] = []
		index[key].append(item)
	return index

def unused_function():
	pass
