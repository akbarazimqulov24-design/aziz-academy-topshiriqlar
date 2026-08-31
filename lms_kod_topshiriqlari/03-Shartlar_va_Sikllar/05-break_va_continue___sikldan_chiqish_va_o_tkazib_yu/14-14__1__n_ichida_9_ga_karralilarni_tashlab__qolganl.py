n = int(input())
yigindi = 0

for i in range(1, n + 1):
  # Agar son 9 ga karrali bo'lsa, tashlab ketamiz (continue)
  if i % 9 == 0:
    continue
  yigindi += i

print(yigindi)