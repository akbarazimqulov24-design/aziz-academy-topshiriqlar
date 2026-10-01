nums = list(map(int, input().split()))

last_digits = {(x * x) % 10 for x in nums}
               
res = sorted(list(last_digits))
               
print(res)               

               