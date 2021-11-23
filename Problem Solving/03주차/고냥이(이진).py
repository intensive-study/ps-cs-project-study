from collections import deque

N = int(input())
lst = list(input())

left, right = 0, 0
ans = 0
alpha = set()

while left <= right < len(lst):
    alpha.add(lst[right])
    right += 1
    
    if len(alpha) <= N:
        ans = max(ans, right - left)        
    else:
        if lst[left] not in lst[left+1:right]:
            alpha.remove(lst[left])
        left += 1
print(ans)