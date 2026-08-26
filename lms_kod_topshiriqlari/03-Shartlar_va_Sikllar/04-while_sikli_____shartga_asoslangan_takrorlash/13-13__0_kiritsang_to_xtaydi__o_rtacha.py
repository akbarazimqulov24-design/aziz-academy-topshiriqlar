yigindi = 0
sanoq = 0

while True:
    n = int(input())
    if n == 0:
        break
    yigindi += n
    sanoq += 1
    
if sanoq == 0:
    print(0)
else:
    print(yigindi / sanoq)