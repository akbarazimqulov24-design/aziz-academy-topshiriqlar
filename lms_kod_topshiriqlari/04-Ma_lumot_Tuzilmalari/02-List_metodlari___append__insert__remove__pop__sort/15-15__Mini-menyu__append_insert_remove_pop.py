import sys

a = []
for line in sys.stdin:
    cmd, *v = line.split()
    if cmd == "stop":
        break
    elif cmd =="append":
        a.append(int(v[0]))
    elif cmd == "insert":
        a.insert(int(v[0]), int(v[1]))
    elif cmd == "remove" and int(v[0]) in a:
        a.remove(int(v[0]))
    elif cmd == "pop" and 0 <= int(v[0]) <len(a):
        a.pop(int(v[0]))
       
print(a)    
        
        