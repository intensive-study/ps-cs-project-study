import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
tree = defaultdict(list)
removed = int(input())
root = -1

for i in range(n):
    p = arr[i]
    if p == -1: 
        root = i
        continue
    
    if i == removed or p == removed: continue

    tree[p].append(i)

def solve(node):
    if node == removed: return 0 # consider if root is deleted.
    if not tree[node]: return 1
    cnt = 0
    for child in tree[node]: cnt += solve(child)

    return cnt

if __name__ == "__main__":
    print(solve(root))