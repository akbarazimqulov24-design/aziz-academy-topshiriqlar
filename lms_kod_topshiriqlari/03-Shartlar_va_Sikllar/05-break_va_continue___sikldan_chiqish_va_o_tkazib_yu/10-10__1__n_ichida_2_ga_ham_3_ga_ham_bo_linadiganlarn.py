n = int(input())

for i in range(1, n + 1):
  # 2 ga va 3 ga bo'linadigan sonlar (ya'ni 6 ga karralilar)
  if i % 2 == 0 and i % 3 == 0:
        continue
  print(i)