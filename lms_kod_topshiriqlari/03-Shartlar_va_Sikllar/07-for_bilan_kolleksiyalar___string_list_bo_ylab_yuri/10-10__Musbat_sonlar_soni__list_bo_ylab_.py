input() # Birinchi qatordagi sonlarvsonini o'tkazib yuboramiz
print(sum(1 for x in map(int, input().split()) if x > 0))