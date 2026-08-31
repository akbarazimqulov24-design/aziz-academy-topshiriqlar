musbat_sonlar_soni = 0

while True:
    son = int(input())
    if son == 0:
        break
    if son < 0:
       continue
    musbat_sonlar_soni += 1
        
print(musbat_sonlar_soni)