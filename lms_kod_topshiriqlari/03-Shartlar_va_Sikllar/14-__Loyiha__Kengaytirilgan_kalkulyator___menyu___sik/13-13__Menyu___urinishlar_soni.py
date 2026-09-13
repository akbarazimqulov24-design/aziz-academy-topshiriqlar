import sys

amal_soni = 0
for line in sys.stdin:
    buyruq = line.strip()
    if buyruq == '0':
        break
    if buyruq in ('1', '2'):
        amal_soni += 1
        
print(amal_soni)