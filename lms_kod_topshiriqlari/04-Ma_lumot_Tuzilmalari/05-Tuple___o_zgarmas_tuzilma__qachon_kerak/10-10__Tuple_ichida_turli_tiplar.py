def parse_val(v):
    for fn in (int, float):
        try: return fn(v)
        except ValueError: pass
    return v

print(tuple(parse_val(x) for x in input().split()))
   