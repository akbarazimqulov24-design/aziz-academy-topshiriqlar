first = input()
last = input()

def make_full_name(first, last):
    return f"{first} {last}"

print(make_full_name(first, last))
print(make_full_name(last=last, first=first))
