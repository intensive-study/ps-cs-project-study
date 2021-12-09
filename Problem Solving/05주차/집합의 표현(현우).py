import sys
sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()

def union(a, b):
    a,b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    w, a, b = map(int, input().split())
    if not w:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')