n = int(input())
print(
    "Yes"
    if sum(1 for i in range(1, n + 1) if n % i == 0) > 2
    else "No"
)