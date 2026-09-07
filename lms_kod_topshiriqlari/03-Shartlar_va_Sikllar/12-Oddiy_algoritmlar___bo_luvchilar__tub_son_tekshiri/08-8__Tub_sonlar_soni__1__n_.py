n = int(input())
print(
    sum(
        all(x % i for i in range(2, int(x**0.5) + 1)) for x in range(2, n + 1)
    )
)