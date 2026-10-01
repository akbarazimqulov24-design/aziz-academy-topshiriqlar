x, lo, hi = map(int, input().split())

def clamp(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
    
print(clamp(x, lo, hi))
print(clamp(lo=lo, hi=hi, x=x))
