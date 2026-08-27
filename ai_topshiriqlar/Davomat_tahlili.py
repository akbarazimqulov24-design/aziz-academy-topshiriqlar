# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: Solishtirish operatorlari — == != > < >= <=
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
s = input().split()
print(s.count('1'))
print(max("".join(s).split('0'), key=len) if '1' in s else 0)