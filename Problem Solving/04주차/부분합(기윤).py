import sys

input = sys.stdin.readline
n, s = map(int, input().split())
seq = tuple(map(int, input().split()))
lp, rp = 0, 1
INF = sys.maxsize
answer = INF
table = [0] * (n+1)

for i in range(n): table[i+1] = table[i] + seq[i]

while lp < n:
    total = table[rp] - table[lp]
    if total >= s:
        answer = min(answer, rp-lp)
        lp += 1
        if lp == rp: rp += 1
    
    else: rp += 1

    if rp > n:
        lp += 1
        rp = lp + 1

if answer == INF: print(0)
else: print(answer)