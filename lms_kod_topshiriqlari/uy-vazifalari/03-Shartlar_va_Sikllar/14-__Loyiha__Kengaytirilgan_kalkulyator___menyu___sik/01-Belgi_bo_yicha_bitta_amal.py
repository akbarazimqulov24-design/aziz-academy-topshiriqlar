a = int(input())
op = input()
b = int(input())

ops = {'+': a + b, '-': a - b, '*': a * b}
print(ops.get(op, "Noma'lum amal"))