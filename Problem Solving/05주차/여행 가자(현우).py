import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
        
N = int(input())
M = int(input())
parent = [i for i in range(N)]
flag = 0
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            a, b = find_parent(i), find_parent(j)
            union(a,b)
ans = list(map(int, input().split()))
for i in range(len(ans)-1):
    a, b = find_parent(ans[i]-1), find_parent(ans[i+1]-1)
    if parent[find_parent(a)] != parent[find_parent(b)]:
        flag = 1
        break
if not flag:
    print("YES")
else:
    print("NO")