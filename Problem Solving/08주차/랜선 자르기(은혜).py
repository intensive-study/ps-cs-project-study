import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
minlen, maxlen = 1, max(cables)

while minlen <= maxlen :
    mid = (minlen + maxlen) // 2
    cnt = 0
    
    for cable in cables:
        cnt += cable // mid
        
    if cnt >= N :
        minlen = mid + 1
    else:
        maxlen = mid - 1

print(maxlen)