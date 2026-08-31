yigindi = 0

while True:
    son = int(input())
    # Agar son toq bo'lsa, siklni to'xtamiz
    if son % 2 != 0:
        break 
    yigindi += son
    
print(yigindi)