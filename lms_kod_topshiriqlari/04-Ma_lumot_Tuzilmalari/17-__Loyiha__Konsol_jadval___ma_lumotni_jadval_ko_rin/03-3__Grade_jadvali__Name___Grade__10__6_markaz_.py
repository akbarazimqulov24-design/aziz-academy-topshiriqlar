n = int(input())
print(f"{'Name':<10} | Grade\n{'-'*10}+{'-'*6}")
for _ in range(n):
    a, b = input().split()
    s = int(b)
    g = 'A' if s>=90 else 'B' if s>=80 else 'C' if s>=70 else 'D' if s>=60 else 'F'
    print(f"{a:<10} |   {g}")