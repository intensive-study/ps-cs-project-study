import sys

sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [-1] * (n+1)

def find(a):
    if arr[a] == -1: return a
    arr[a] = find(arr[a])
    return arr[a]
    
def merge(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    arr[pa] = pb

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0: merge(a, b)
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb: print("YES")
        else: print("NO")