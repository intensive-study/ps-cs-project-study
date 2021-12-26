import sys

input = sys.stdin.readline

n = int(input())
table = [True] * (n+1)
for i in range(2): table[i] = False

for i in range(2, n+1):
    if table[i]:
        for j in range(i*i, n+1, i): table[j] = False

i = 0
answer = 0

while True:
    while i < n+1 and not table[i]: i += 1
    if i == n+1: break
    ok = False
    total = 0

    for j in range(i, n+1):
        if table[j]: total += j
        if total >= n:
            if total == n: ok = True
            break
    
    if ok: answer += 1
    i += 1

print(answer)