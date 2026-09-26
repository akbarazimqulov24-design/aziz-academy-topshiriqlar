import sys

input_data = sys.stdin.read().splitlines()
a = set(map(int, input_data[0].split()))
b = set(map(int, input_data[1].split()))
print("Ha" if a.issubset(b) else "Yoq")