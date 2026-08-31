# Kirish ma'lumotlarini o'qib olish
tur = int(input())
qiymat = int(input())

# Shartlar bo'yicha konvertatsiya qilish
if tur == 1:
    print(qiymat * 1000)
elif tur == 2:
    print(qiymat * 60)
elif tur == 3:
    print(qiymat * 1000)
else:
    print("Notogri tanlov")