words = input().split()
langest = ""
for w in words:
    if len(w) > len(langest):
        langest = w
print(langest)