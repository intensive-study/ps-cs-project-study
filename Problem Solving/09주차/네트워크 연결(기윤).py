import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
adj = []
uf = [-1] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    adj.append((a, b, c))

def find(a):
    if uf[a] == -1: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    pa = find(a)
    pb = find(b)

    if pa == pb: return False
    
    uf[pb] = pa
    return True

adj.sort(key=lambda x: x[-1])
total = 0
cnt = 0

for src, dst, cost in adj:
    if merge(src, dst):
        total += cost
        cnt += 1
    
    if cnt == n-1: break

print(total)