s = input()
old = input()
new = input()

def replace_cher(s, old, new):
    return s.replace(old, new)

print(replace_cher(s, old, new))
print(replace_cher(new=new, s=s, old=old))