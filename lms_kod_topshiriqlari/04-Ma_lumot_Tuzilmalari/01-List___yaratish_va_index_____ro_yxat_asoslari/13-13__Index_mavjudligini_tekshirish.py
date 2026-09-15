n = int(input())
lst = list(map(int, input().split()))

# 5-indeks mavjudligini tekshirish (uzunligi 5 dan katta, ya'ni kamida 6 ta element bo'lishi kerak)
if len(lst) > 5:
    print(lst[5])
else:
    print('Error')