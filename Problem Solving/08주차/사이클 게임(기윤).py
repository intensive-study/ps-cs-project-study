import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(5e5))

def find(a):
    if uf[a] == -1: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb: return False
    if pa < pb: uf[pb] = pa
    else: uf[pa] = pb
    return True

n, m = map(int, input().split())
uf = [-1] * n
pairs = []
for i in range(1, m+1):
    a, b = map(int, input().split())
    pairs.append((a, b))

answer = 0
for i, pair in enumerate(pairs):
    if not merge(pair[0], pair[1]):
        answer = i + 1
        break

print(answer)