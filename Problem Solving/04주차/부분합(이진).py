# 반례 모음: https://bingorithm.tistory.com/13

'''
시간초과
'''
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
minLen = len(lst)

for num in lst:
    if num>=s:
        minLen = 1
        break

l, r = 0, 1
while l < r:
    # print(lst[l:r+1], sum(lst[l:r+1]))
    
    if sum(lst[l:r+1])>= s:
        minLen = min(minLen, r-l+1)
        # print('minLen: ',minLen)
        l += 1
    else:
        r += 1
print(minLen)         
'''

'''
solution2 144ㅡms
'''
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

def solve(s, lst):
    minLen = 100001
    total = 0
    l, r = 0, 0
    while True:
        if total >= s:
            minLen = min(minLen, r-l)
            total -= lst[l]
            l += 1     
        elif r == n:
            break
        else:
            total += lst[r]
            r += 1
    if minLen == 100001:
        return 0
    else:
        return minLen



print(solve(s, lst))