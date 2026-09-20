a, b = int(input()), int(input())
print(*{"sum": a + b, "product": a * b}.values(), sep="\n")