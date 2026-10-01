w, h = map(int, input().split())

def rect_area(w, h):
    return w * h

print(rect_area(w, h))
print(rect_area(h=h, w=w))