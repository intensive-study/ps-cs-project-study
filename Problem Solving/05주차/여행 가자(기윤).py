import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

is_connected = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
nodes = list(map(int, sys.stdin.readline().rstrip().split()))

p = [-1 for _ in range(n+1)]

def find(node):
    if p[node] < 0: return node
    p[node] = find(p[node])
    return p[node]

def merge(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb: return

    p[pb] = pa

for i in range(n):
    for j in range(n):
        if is_connected[i][j]: merge(i+1, j+1)

ok = True
root = find(nodes[0])

for i in range(1, m):
    if root != find(nodes[i]):
        ok = False
        break  

if ok: print('YES')
else: print('NO')