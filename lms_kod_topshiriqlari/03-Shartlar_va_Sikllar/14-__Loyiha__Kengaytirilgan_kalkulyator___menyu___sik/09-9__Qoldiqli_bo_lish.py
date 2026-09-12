import sys

# Barcha qatordagi ma'lumotlarni bitta umumiy ro'yxatga o'qib olamiz
data = sys.stdin.read().split()
a = int(data[0])
b = int(data[1])
tanlov = int(data[2])

if tanlov == 5:
    print(a % b)