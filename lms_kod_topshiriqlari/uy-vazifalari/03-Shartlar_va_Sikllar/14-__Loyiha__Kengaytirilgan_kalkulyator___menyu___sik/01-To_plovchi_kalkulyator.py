res = 0

while True:
    op = input().strip()
    if op == "=":
        break
        
    num = int(input())
    if op == "+":
        res += num
    elif op == "-":
        res -=num
    elif op == "*":
        res *= num
    elif op == "/":
        if num != 0:
            res //= num
            
print(res)            
        
    