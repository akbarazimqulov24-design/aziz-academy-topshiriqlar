def stats(nums):
    return {
        'count': len(nums),
        'sum': sum(nums),
        'min': min(nums),
        'max': max(nums)
    }
        
# Kiruvchi ma'lumot o'qib olish va ro'yxatga o'tkazish
nums = list(map(int, input().split())) 
        
# Natija chiqarish
print(stats(nums))