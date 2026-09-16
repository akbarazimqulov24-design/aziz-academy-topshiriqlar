n = int(input()) 
sonlar = list(map(int, input().split()))

manfiy_sonlar = [x for x in sonlar if x < 0]

print(manfiy_sonlar)