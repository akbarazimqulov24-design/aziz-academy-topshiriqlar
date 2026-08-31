n = int(input())
juft_sonlar_soni = 0
oxirgi_juft = "No"

i = 1
while i <= n:
    if i % 2 == 0:
       juft_sonlar_soni += 1
       oxirgi_juft = i
       if juft_sonlar_soni == 3:
         break
    i += 1
    
 # Agar 3 ta juft son topilmagan bo'lsa, natija "No" ga qaytaramiz
if juft_sonlar_soni < 3:
    oxirgi_juft = "No"
    
print(oxirgi_juft)