import sys
input = sys.stdin.readline

def find(target):
	if target == parent[target]:
		return target
	else:
		root_target = find(parent[target])
		parent[target] = root_target
		return parent[target]

def union(a, b):
	root_a = find(a)
	root_b = find(b)
	if root_a != root_b:
		parent[root_b] = root_a
		count[root_a] += count[root_b]

for _ in range(int(input())):# test case
	parent = dict()
	count = dict()

	for _ in range(int(input())): # 친구 관계 수
		a, b = input().split()
		if a not in parent:
			parent[a] = a
			count[a] = 1
		if b not in parent:
			parent[b] = b
			count[b] = 1

		union(a, b)
		print(count[find(a)])
