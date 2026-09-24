import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    students = [{'name': data[1 + i*2], 'score': int(data[2 + i*2])} for i in range(n)]
    
    best = min(students, key=lambda x: (-x['score'], x['name']))
    print(best['name'], best['score'])