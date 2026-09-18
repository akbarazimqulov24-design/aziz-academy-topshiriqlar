char = input()
text = input()

count = 0
for ch in text:
    if ch == char:
        count += 1
        
print(count)