import sys
input = sys.stdin.readline

def find(target):
	if target == parent[target]:
		return target
	else:
		parent[target] = find(parent[target])
		return parent[target]

def union(a, b):
	root_a = find(a)
	root_b = find(b)
	if root_a < root_b:
		parent[root_b] = root_a
	else:
		parent[root_a] = root_b

n, m = map(int, input().split())
parent = [i for i in range(n)]
for i in range(m):
	a, b = map(int, input().split())
	if find(a) == find(b):
		print(i+1)
		break
	union(a,b)
else:
	print(0)