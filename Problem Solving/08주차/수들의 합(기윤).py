import sys

n, m = map(int, sys.stdin.readline().rsplit())
arr = list(map(int, sys.stdin.readline().rsplit()))
sp, ep = 0, 0
answer = 0

while ep < n:
    total = sum(arr[sp:ep+1])
    if total == m:
        answer += 1
        ep += 1
    elif sp == ep: ep += 1
    elif total > m: sp += 1
    else: ep += 1

print(answer)