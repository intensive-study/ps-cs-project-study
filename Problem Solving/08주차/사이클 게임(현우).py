import sys

def input():
    return sys.stdin.readline().rstrip()

def union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

N, M = map(int, input().split())
parent = [i for i in range(N)]
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    if find_parent(a) != find_parent(b):
        union(a,b)
    else:
        ans = i+1
        break
print(ans)